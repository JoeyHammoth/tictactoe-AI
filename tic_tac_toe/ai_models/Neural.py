import tensorflow as tf
from keras import layers
from main_assets.Board import Board
from ai_models.Random import Random
import copy

import numpy as np

class Nueral:
    """
    A class to represent a Neural Network AI for Tic-Tac-Toe. Uses a tensorflow neural network to predict the best move. 

    Methods:
    - create_tictactoe_model: Creates a neural network model for Tic-Tac-Toe
    - move_to_one_hot: Converts a move to a one-hot encoding
    - play_game: Plays a game of Tic-Tac-Toe with a random AI
    - train_tictactoe_model: Trains the neural network model on a number of games
    - generate_answer: Generates the best move for the current board state
    """
    def __init__(self, games):
        self.model = self.train_tictactoe_model(games)

    def create_tictactoe_model(self):
        """
        Creates a neural network model for Tic-Tac-Toe. The model has 9 input nodes (one for each cell in the board), 
        64 hidden nodes, and two output nodes (policy and value). The policy output is a softmax layer with 9 nodes, 
        and the value output is a single node with a tanh activation. 

        Args:
        - None

        Returns:
        - model (tf.keras.Model): An untrained neural network model for Tic-Tac-Toe 
        """

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
        """
        Converts a move to a one-hot encoding. The one-hot encoding is a 9-element array with a 1 at the index of the move. 

        Args:
        - move (tuple): The move to convert to a one-hot encoding
        - player (int): The player making the move (1 for Circle, 2 for Cross)

        Returns:
        - np.array: A one-hot encoding of the move
        """

        board = [0,0,0,0,0,0,0,0,0]
        index = move[1] * 3 + move[0]
        board[index] = player
        return np.array(board) 
    
    def play_game(self):
        """
        Plays a game of Tic-Tac-Toe with a random AI. The game is played until there is a winner or a draw. 

        Args:
        - None

        Returns:
        - states (list): A list of board states during the game
        - moves (list): A list of moves made during the game
        - results (list): A list of results for each state (1 for Circle win, -1 for Cross win, 0 for draw) 
        """

        random_ai = Random()
        board = Board()  # Initialize an empty board
        board.board_list = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
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
    
    def train_tictactoe_model(self, games, epochs=10, batch_size=32):
        """
        Trains the neural network model on a number of games. The model is trained using the states, moves, and results from the games.

        Args:
        - games (int): The number of games to play and train on
        - epochs (int): The number of epochs to train the model
        - batch_size (int): The batch size for training the model

        Returns:
        - model (tf.keras.Model): The trained neural network model
        """
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
        """
        Generates the best move for the current board state. The best move is determined by the policy output of the neural network model.

        Args:
        - board (Board): The current game board

        Returns:
        - tuple: The best move coordinate tuple
        """
        
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