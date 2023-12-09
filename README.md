# Tic-Tac-Toe

Tic-tac-toe is a classic two-player game that is played on a 3x3 grid. The players take turns marking a square with their designated symbol, usually "X" for one player and "O" for the other. The goal of the game is to get three of your symbols in a row, either horizontally, vertically, or diagonally.

## Here are the basic rules:

### Game Setup:
The game is played on a 3x3 grid.
Players decide who goes first; one player is "X," and the other is "O."

### Gameplay:
* Players take turns placing their symbol in an empty square on the grid.
* Once a square is marked, it cannot be changed or overwritten.

### Winning:
* A player wins by having three of their symbols in a row horizontally, vertically, or diagonally.
* If the entire grid is filled and no player has three in a row, the game is a draw.

### Strategy:
* The key to winning is blocking your opponent from getting three in a row while also trying to create your own winning sequences.

## Minimax Algorithm
The Minimax algorithm is a strategy used in two-player games, and it's particularly well-suited for games like tic-tac-toe. The goal of Minimax is to find the best move for a player, assuming that the opponent will also make optimal moves. It's called "Minimax" because it involves minimizing the possible loss for the worst-case scenario and maximizing the potential gain for the best-case scenario.

## Here's how the Minimax algorithm works in the context of tic-tac-toe:

### Evaluation Function:
* Each leaf node of the game tree (a possible board configuration) is assigned a value. In the case of tic-tac-toe, this value could be +1 for a win, -1 for a loss, and 0 for a draw.

### Recursive Search:
* The algorithm recursively explores the game tree, starting from the current board state and considering all possible future moves.

### Maximizing and Minimizing:
* The algorithm alternates between two players, the maximizing player (trying to maximize its score, usually representing the AI) and the minimizing player (trying to minimize the score, representing the opponent).
* At each level of the tree, the maximizing player chooses the move with the highest value, and the minimizing player chooses the move with the lowest value.

### Backtracking:
* As the algorithm explores deeper levels of the tree, it keeps track of the best move at each level, backtracking towards the root.

### Optimal Move:
* Once the entire tree is explored, the algorithm returns the move that leads to the best outcome for the current player, assuming optimal play from both sides.

## Here's a high-level overview of the process:

### Maximizing Player's Turn:
* The maximizing player considers all possible moves and chooses the one with the highest value.

### Minimizing Player's Turn:
* The minimizing player considers all possible responses to the maximizing player's move and chooses the one with the lowest value.

### Repeat:
* The process continues until a terminal state is reached (win, lose, or draw).

By systematically exploring the game tree and considering all possible outcomes, Minimax ensures that the player makes the best move based on the assumption that the opponent will also make optimal moves. In the case of tic-tac-toe, the algorithm guarantees that the player will never lose if a winning move is available, and it will aim for a draw if no winning move is possible.

## Code Explanation 

### Initialization: 
The game starts with an empty grid and a variable to track whose turn it is (playerTurn).

### Game Loop: 
The main game loop continues until there is a winner or a draw. In each iteration, it alternates between the player and the agent.

### Display Grid: 
The drawGrid function is responsible for displaying the current state of the grid.

### Player's Move: 
The player is prompted to enter their move, and input validation is performed to ensure the move is valid.

### Agent's Move: 
The agent's move is determined using the Min-Max algorithm in the getAgentsMove function.

### Min-Max Algorithm: 
The miniMax function implements the Min-Max algorithm to determine the best move for the agent. It considers the current state of the grid and recursively explores possible moves.

### Check Winner and Draw: 
Functions checkWinner and checkDraw are used to determine if there is a winner or if the game is a draw.

### Game Outcome: 
The game prints messages indicating the outcome (winner, draw) and continues until the game is over.

## Code Execution
> python3 MiniMax.py