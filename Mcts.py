import math
import random

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state  # The game state at this node
        self.parent = parent  # Parent node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Value of this node (wins-losses)
        self.move = move
    
class Mcts:
    def __init__(self):
        pass

    def best_child(self, node, criterion):
        if criterion == 'uct':
            c = 1.414  # Exploration parameter
            return max(node.children, key=lambda child: (child.value / child.visits) +
                    c * math.sqrt(math.log(node.visits) / child.visits))
        elif criterion == 'visits':
            return max(node.children, key=lambda child: child.visits)
    
    def apply_move(self, state, move, red):
        new_state = state
        new_state.flip(red, move[0], move[1])
        return new_state

    def get_result(self, current_state, red):
        if red:
            if current_state.check_board == 1:
                return 1
            elif current_state.check_board == 2:
                return -1
            else:
                return 0
        else:
            if current_state.check_board == 1:
                return -1
            elif current_state.check_board == 2:
                return 1
            else:
                return 0
            
    def select(self, node):
        while node.children:
            node = self.best_child(node, criterion='uct')
        return node

    def expand(self, node, red):
        possible_moves = node.state.get_valid_moves() # Generate legal moves list
        for move in possible_moves:
            new_state = self.apply_move(node.state, move, red) # Return a new board that includes the move
            child_node = Node(state=new_state, parent=node, move=move)
            node.children.append(child_node)
        return random.choice(node.children)  # Return a random child for simulation
    
    def simulate(self, state, red):
        current_state = state
        while (current_state.check_board() == 0):  # Play until the game ends
            move = random.choice(current_state.get_valid_moves())
            current_state = self.apply_move(current_state, move, red)
        return self.get_result(current_state, red)  # Return 1 for win, -1 for loss, 0 for draw

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.value += result  # Increment value by simulation result
            result = -result  # Alternate result for opponent's perspective
            node = node.parent

    def mcts(self, root, iterations, red):
        # _ is dummy
        for _ in range(iterations):
            # Step 1: Selection
            leaf = self.select(root)
            
            # Step 2: Expansion
            if leaf.state.check_board() == 0:  # If the game is not over
                child = self.expand(leaf, red)
            else:
                child = leaf
            
            # Step 3: Simulation
            result = self.simulate(child.state, red)
            
            # Step 4: Backpropagation
            self.backpropagate(child, result)

        # Return the child with the highest visit count
        best_node = self.best_child(root, criterion='visits')
        return best_node.move

    def generate_answer(self, board):
        # Initialize root node with the current game state
        root = Node(board)

        # Run MCTS
        best_move = self.mcts(root, iterations=1000)

        return best_move