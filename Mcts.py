class node:
    def __init__(self, state, parent=None):
        self.state = state  # The game state at this node
        self.parent = parent  # Parent node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Value of this node (wins-losses)
    
    
    