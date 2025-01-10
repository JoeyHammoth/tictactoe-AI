import math

class node:
    def __init__(self, state, parent=None):
        self.state = state  # The game state at this node
        self.parent = parent  # Parent node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Value of this node (wins-losses)
    
class mcts:
    def __init__(self):
        pass

    def best_child(self, node, criterion):
        if criterion == 'uct':
            c = 1.414  # Exploration parameter
            return max(node.children, key=lambda child: (child.value / child.visits) +
                    c * math.sqrt(math.log(node.visits) / child.visits))
        elif criterion == 'visits':
            return max(node.children, key=lambda child: child.visits)
    
    def select(self, node):
        while node.children:
            node = self.best_child(node, criterion='uct')
        return node

    
    def expand(self, node):
        possible_moves = node.state.get_valid_moves() # Generate legal moves list
        for move in possible_moves:
            new_state = apply_move(node.state, move)
            child_node = Node(state=new_state, parent=node)
            node.children.append(child_node)
        return random.choice(node.children)  # Return a random child for simulation
    
    def simulate(self, state):
        current_state = state
        while (current_state.check_board() == 0):  # Play until the game ends
            move = random.choice(get_legal_moves(current_state))
            current_state = apply_move(current_state, move)
        return get_result(current_state)  # Return 1 for win, -1 for loss, 0 for draw

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.value += result  # Increment value by simulation result
            result = -result  # Alternate result for opponent's perspective
            node = node.parent