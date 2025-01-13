import tensorflow as tf
from keras import layers, models
from Board import Board
from Random import Random
import copy

import numpy as np

class Nueral:
    def __init__(self):
        self.model = self.train_tictactoe_model()

    def create_tictactoe_model(self):
        # model = tf.keras.Sequential([
        #     layers.Input(shape=(9,)),  # 9 cells in the board
        #     layers.Dense(64, activation='relu'),
        #     layers.Dense(64, activation='relu'),
        #     layers.Dense(9, activation='softmax'),  # Policy output (move probabilities)
        #     layers.Dense(1, activation='tanh')     # Value output (-1 to 1)
        # ])
        # return model

        input_layer = layers.Input(shape=(9,))  # 9 cells in the board
        
        # Shared hidden layers
        x = layers.Dense(64, activation='relu')(input_layer)
        x = layers.Dense(64, activation='relu')(x)

        # Policy head
        policy_head = layers.Dense(9, activation='softmax', name='policy')(x)

        # Value head
        value_head = layers.Dense(1, activation='tanh', name='value')(x)

        # Create the model with two outputs
        model = tf.keras.Model(inputs=input_layer, outputs=[policy_head, value_head])
        return model

    def move_to_one_hot(self, move, player):
        board = [0,0,0,0,0,0,0,0,0]
        index = move[1] * 3 + move[0]
        board[index] = player
        return np.array(board) 
    
    def play_game(self):
        random_ai = Random()
        board = Board()  # Initialize an empty board
        states, moves, results = [], [], []
        current_player = 1  # 1 is Circle, 2 is Cross

        while board.check_board() == 0:
            np_board = np.array(board.board_list)
            np_board_1D = np_board.flatten()
            states.append(np_board_1D)
            
            # Random AI Move 
            valid = False
            while valid == False:
                answer = random_ai.generate_answer()
                if (board.is_valid_move(answer[0], answer[1]) == True):
                    valid = True
            move = answer

            moves.append(self.move_to_one_hot(move, current_player))  # One-hot encoding of the move
            player_bool = True if current_player == 1 else False
            board.flip(player_bool, move[0], move[1])
            
            current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)

        if board.check_board() == 1: # 1 for Circle win, -1 for Cross win, 0 for draw
            result = 1
        elif board.check_board() == 2:
            result = -1
        else:
            result = 0

        results = [result] * len(states)
        return states, moves, results
    
    def train_tictactoe_model(self, games=1000, epochs=10, batch_size=32):
        states, policies, values = [], [], []
        for _ in range(games):
            s, p, v = self.play_game()
            states.extend(s)
            policies.extend(p)
            values.extend(v)

        states = np.array(states)
        policies = np.array(policies)
        values = np.array(values)

        # Normalize board state
        states = np.where(states == 2, -1, states)

        model = self.create_tictactoe_model()

        model.compile(
            optimizer='adam',
            loss=['categorical_crossentropy', 'mse'],  # Policy and value loss
            loss_weights=[1.0, 1.0]
        )
        model.fit(states, [policies, values], epochs=epochs, batch_size=batch_size)
        return model

    def generate_answer(self, board):
        g_board = copy.deepcopy(board.board_list)
        state = np.array(g_board)
        state = state.flatten()
        
        state = np.where(state == 2, -1, state).reshape(1, -1)  # Convert 2 to -1 for model input
        policy, _ = self.model.predict(state)  # Get predicted policy and value from the model

        legal_moves = board.get_valid_moves() # List of tuples, e.g., [(0, 0), (0, 1), ...]
        policy = np.squeeze(policy)  # Flatten the policy output (shape: [9])

        # Convert legal moves to their flattened indices
        legal_indices = [row * 3 + col for col, row in legal_moves]

        # Extract probabilities for legal moves
        legal_probs = [policy[idx] for idx in legal_indices]

        # Choose the move with the highest probability
        best_move_index = np.argmax(legal_probs)
        best_move = legal_moves[best_move_index]

        return best_move  # Return the (row, col) tuple