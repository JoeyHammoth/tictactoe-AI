# Tic Tac Toe AI Project

## Introduction
This project is a study in adversarial AI game-playing algorithms and strategies, centered around the classic game of Tic Tac Toe. It investigates various AI approaches to enhance decision-making and gameplay efficiency. The implemented algorithms include:

- **Random Move Selection**
- **Minimax with Alpha-Beta Pruning**
- **Monte Carlo Tree Search (MCTS)**
- **Multi-Layer Perceptron (MLP)**

The project is implemented in Python and is designed to facilitate learning and experimentation with these AI techniques. Latest release can be found [here](https://github.com/JoeyHammoth/tictactoe-AI/releases/tag/v.1.0).

---

## Features
- **Game Implementation**: A fully functional Tic Tac Toe game.
- **AI Strategies**: Multiple adversarial algorithms, allowing comparisons of strengths and weaknesses.
- **Customizable Gameplay**: Play against AI or observe AI vs. AI matches.
- **Performance Metrics**: Analyze the efficiency and decision-making quality of each algorithm.

---

## Project Structure
```bash
tic_tac_toe
├── Main.py
├── Main.spec
├── __init__.py
├── __pycache__
│   ├── Main.cpython-311.pyc
│   └── __init__.cpython-311.pyc
├── ai_models
│   ├── MCTS.py
│   ├── Minimax.py
│   ├── Neural.py
│   ├── Random.py
│   ├── __init__.py
│   └── __pycache__
│       ├── MCTS.cpython-311.pyc
│       ├── Minimax.cpython-311.pyc
│       ├── Neural.cpython-311.pyc
│       ├── Random.cpython-311.pyc
│       └── __init__.cpython-311.pyc
├── icon.png
└── main_assets
    ├── AppBoard.py
    ├── Board.py
    ├── Master.py
    ├── __init__.py
    └── __pycache__
        ├── AppBoard.cpython-311.pyc
        ├── Board.cpython-311.pyc
        ├── Master.cpython-311.pyc
        └── __init__.cpython-311.pyc
```

## Documentation
For documentation regarding this library of packages, the javadoc can be accessed [here](https://joeyhammoth.github.io/tictactoe-AI/tic_tac_toe.html).
For more information regarding usage, the wiki can be accessed [here](https://github.com/JoeyHammoth/tictactoe-AI/wiki).

## Requirements

### Software Dependencies
- Python 3.8+
- Required libraries:
  - `numpy` (for the MLP approach and analysis)
  - `keras` (for the MLP approach)
  - `matplotlib` (for visualization in analysis)
  - `tensorflow` (for the MLP approach)
  - `tkinter` (for GUI)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/JoeyHammoth/tictactoe-AI.git
   cd tictactoe-AI
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
---

## Usage

### Running the Game
Run the main script to start the game:
```bash
python Main.py
```

### Modes
- **Player vs. AI**: Play against any AI strategy.
- **AI vs. AI**: Watch two AI strategies compete.

### Configurations
You can configure the following in the application:
- AI strategies for each player.
- Minimax max depth for evaluation function.
- Monte Carlo simulation iterations and exploration parameter.
- MLP training parameters.

---

## Algorithm Details

### Random Move Selection
The AI chooses a random empty cell for its move. This serves as a baseline strategy.

### Minimax with Alpha-Beta Pruning
This algorithm evaluates all possible moves to maximize its own advantage while minimizing the opponent's. Alpha-beta pruning optimizes the search by cutting off branches that won't affect the outcome.

### Monte Carlo Tree Search (MCTS)
MCTS builds a search tree using random simulations to estimate the best moves. It balances exploration and exploitation for decision-making.

### Multi-Layer Perceptron (MLP)
A neural network model trained on historical game data to predict optimal moves based on the current board state.

---

## Evaluation
- **Win/Loss Statistics**: Analyze AI performance over multiple games.
- **Search Depth**: Compare decision times for different algorithms.
- **Strategy Analysis**: Evaluate the effectiveness of each approach in various game scenarios.

---

## Future Work
- Extend to larger grids (e.g., 4x4, 5x5).
- Experiment with reinforcement learning.
- Optimize MLP training with larger datasets.
- Implement a graphical user interface (GUI).

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Authors
- **JoeyHammoth** - [My GitHub Profile](https://github.com/JoeyHammoth)

## Acknowledgments
Special thanks to the open-source community for providing tools and resources that made this project possible.


