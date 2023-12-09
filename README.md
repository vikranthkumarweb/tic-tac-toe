# Tic-Tac-Toe

Tic-tac-toe is a classic two-player game that is played on a 3x3 grid. The players take turns marking a square with their designated symbol, usually "X" for one player and "O" for the other. The goal of the game is to get three of your symbols in a row, either horizontally, vertically, or diagonally.

## Here are the basic rules:

### Game Setup:

The game is played on a 3x3 grid.
Players decide who goes first; one player is "X," and the other is "O."

### Gameplay:

Players take turns placing their symbol in an empty square on the grid.
Once a square is marked, it cannot be changed or overwritten.

### Winning:

A player wins by having three of their symbols in a row horizontally, vertically, or diagonally.
If the entire grid is filled and no player has three in a row, the game is a draw.

### Strategy:

The key to winning is blocking your opponent from getting three in a row while also trying to create your own winning sequences.

### Minimax Algorithm

The Minimax algorithm is a decision-making algorithm used in two-player turn-based games, such as tic-tac-toe, chess, or checkers. Its primary goal is to find the optimal move for a player, assuming that the opponent is also playing optimally. The algorithm considers all possible future moves and outcomes to determine the best move.

## Here's a simplified explanation of how the Minimax algorithm works:

### Tree Representation:

The game is represented as a decision tree, where each node represents a possible game state, and each edge represents a possible move.

### Evaluation Function:

Each leaf node of the tree is evaluated using an "evaluation function." In the context of games like tic-tac-toe, this function assigns a score to each terminal state (win, lose, or draw).

### Maximizing and Minimizing:
The algorithm alternates between two players: the "maximizing player" (usually the AI) and the "minimizing player" (the opponent).
The maximizing player aims to maximize the score, while the minimizing player aims to minimize the score.

### Recursion:

Starting from the root of the tree (current game state), the algorithm recursively explores possible moves, creating a subtree for each move.
At each level, the maximizing player chooses the move with the highest score, while the minimizing player chooses the move with the lowest score.

# Backtracking:

As the recursion goes deeper, the scores are propagated back up the tree. The algorithm keeps track of the best score at each level.

### Optimal Move:

Once the entire tree is explored, the algorithm returns the move that leads to the highest score for the maximizing player. This is considered the optimal move assuming both players play optimally.

In summary, Minimax explores all possible game states, assigning scores to terminal states and backtracking to determine the best move for the current player. While effective for small games like tic-tac-toe, the exponential growth in the number of possibilities makes Minimax impractical for larger games without additional optimizations, such as alpha-beta pruning.

## Code Execution

> python3 MiniMax.py