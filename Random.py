import random

class Random:
    def __init__(self):
        pass

    def generate_answer(self, board):
        return (random.randint(0,2), random.randint(0,2))