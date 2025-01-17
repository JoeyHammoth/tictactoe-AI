import math
import random

class Node:
    """
    Node class for the Monte Carlo Tree Search algorithm (MCTS) used in the AI model. 

    Attributes:
    - state: The game state at this node
    - parent: Parent node
    - children: List of child nodes
    - visits: Number of times this node has been visited
    - value: Value of this node (wins-losses)
    - move: The move that led to this node
    """

    def __init__(self, state, parent=None, move=None):
        self.state = state  # The game state at this node
        self.parent = parent  # Parent node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Value of this node (wins-losses)
        self.move = move
    
class Mcts:
    """
    Monte Carlo Tree Search (MCTS) algorithm for the AI model. 

    Attributes:
    - red: Boolean value indicating if the AI is playing as red
    - c: Exploration parameter
    - iterations: Number of iterations to run MCTS

    Methods:
    - best_child: Returns the child node with the highest UCT value
    - apply_move: Returns the new game state after applying a move
    - get_result: Returns the result of the game from the perspective of the AI
    - select: Selects a child node to explore
    - expand: Expands a node by generating child nodes
    - simulate: Simulates a game from a given state
    - backpropagate: Updates the visit count and value of nodes in the tree
    - mcts: Runs the MCTS algorithm
    - generate_answer: Generates the best move for the AI
    """

    def __init__(self, red, c, iterations):
        self.red = red
        self.c = c
        self.iterations = iterations

    def best_child(self, node, criterion):
        """
        Returns the child node with the highest UCT value. 

        Args:
        - node: The parent node
        - criterion: The criterion to use for selecting the best child node (UCT or visits)

        Returns:
        The child node with the highest UCT value or visit count based on the criterion provided
        """

        if criterion == 'uct':
            # c = 1.414  # Exploration parameter
            return max(
                node.children,
                key=lambda child: (child.value / child.visits if child.visits > 0 else float('inf')) +
                                self.c * math.sqrt(math.log(max(1, node.visits)) / (child.visits + 1e-6))  # Avoid division by zero
            )
        elif criterion == 'visits':
            return max(node.children, key=lambda child: child.visits)

    def apply_move(self, state, move):
        """
        Returns the new game state after applying a move. 

        Args:
        - state: The current game state
        - move: The move to apply

        Returns:
        The new game state after applying the move 
        
        """

        new_state = state
        new_state.flip(self.red, move[0], move[1])
        return new_state

    def get_result(self, current_state):
        """
        Returns the result of the game from the perspective of the AI. 

        Args:
        current_state: The current game state

        Returns:
        1 if the AI wins, -1 if the AI loses, and 0 if the game is a draw
        
        """
        if self.red:
            if current_state.check_board() == 1:
                return 1
            elif current_state.check_board() == 2:
                return -1
            else:
                return 0
        else:
            if current_state.check_board() == 1:
                return -1
            elif current_state.check_board() == 2:
                return 1
            else:
                return 0
            
    def select(self, node):
        """
        Selects a child node to explore using the UCT criterion. 

        Args:
        node: The parent node
        
        Returns:
        The child node to explore
        """

        while node.children:
            node = self.best_child(node, criterion='uct')
        return node

    def expand(self, node):
        """
        Expands a node by generating child nodes. 

        Args:
        node: The node to expand

        Returns:
        A child node to explore
        """

        if node.state.check_board() != 0:
            return node
        
        possible_moves = node.state.get_valid_moves() # Generate legal moves list
        for move in possible_moves:
            new_state = self.apply_move(node.state, move) # Return a new board that includes the move
            child_node = Node(state=new_state, parent=node, move=move)
            node.children.append(child_node)
        return random.choice(node.children)  # Return a random child for simulation
    
    def simulate(self, state):
        """
        Simulates a game from a given state. 

        Args:
        state: The game state to simulate from

        Returns:
        1 if the AI wins, -1 if the AI loses, and 0 if the game is a draw
        
        """
        current_state = state
        while (current_state.check_board() == 0):  # Play until the game ends
            move = random.choice(current_state.get_valid_moves())
            current_state = self.apply_move(current_state, move)
        return self.get_result(current_state)  # Return 1 for win, -1 for loss, 0 for draw

    def backpropagate(self, node, result):
        """
        Updates the visit count and value of nodes in the tree. 

        Args:
        - node: The node to backpropagate from
        - result: The result of the simulation

        Returns:
        None
        
        """
        while node is not None:
            node.visits += 1
            node.value += result  # Increment value by simulation result
            result = -result  # Alternate result for opponent's perspective
            node = node.parent

    def mcts(self, root, iterations):
        """
        Runs the Monte Carlo Tree Search (MCTS) algorithm. 

        Args:
        - root: The root node of the tree
        - iterations: Number of iterations to run MCTS

        Returns:
        The best move for the AI to play 
        
        """
        # Ensure root node has children by expanding it first
        if not root.children:
            self.expand(root)  # Expand the root node to generate children
        # _ is dummy
        for _ in range(iterations):
            # Step 1: Selection
            leaf = self.select(root)
            
            # Step 2: Expansion
            if leaf.state.check_board() == 0:  # If the game is not over
                child = self.expand(leaf)
            else:
                child = leaf
            
            # Step 3: Simulation
            result = self.simulate(child.state)
            
            # Step 4: Backpropagation
            self.backpropagate(child, result)

        # Return the child with the highest visit count
        best_node = self.best_child(root, criterion='visits')
        return best_node.move

    def generate_answer(self, board):
        """
        Generates the best move for the AI. 

        Args:
        board: The current game state

        Returns:
        The best move for the AI to play 
        
        """
        # Initialize root node with the current game state
        root = Node(board)

        # Run MCTS
        best_move = self.mcts(root, self.iterations)

        return best_move