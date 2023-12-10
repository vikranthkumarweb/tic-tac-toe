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

# Minimax Algorithm
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

### startPlayingGame Function:
* Initializes the game grid, which is a list representing the Tic Tac Toe board with 9 cells.
* Alternates turns between the player and the AI agent until the game is won or drawn.
* Calls other functions to get moves from the player and the AI, updates the grid, and checks for a winner or draw.

### drawGrid Function:
* Prints the current state of the Tic Tac Toe board.

### getPlayersMove Function:
* Takes user input for the player's move.
* Validates the input to ensure it is a digit between 1 and 9 and that the chosen cell is empty.
* Returns the index of the chosen cell in the grid.

### getAgentsMove Function:
* Implements the AI agent's move using the Min-Max algorithm.
* Iterates through empty cells on the board, simulates placing the AI's symbol (O) in each empty cell, and evaluates the resulting score using the miniMax function.
* Returns the index of the best move for the AI.

### miniMax Function:
* Recursively evaluates the game state to determine the optimal move for the AI.
* Returns a score (-1 for loss, 0 for draw, 1 for win) based on the current state of the board.
* The function alternates between maximizing (AI's turn) and minimizing (player's turn) to find the best move.

### checkWinner Function:
* Checks if any of the winning combinations are present on the board.
* Returns True if there is a winner, False otherwise.

### checkDraw Function:
* Checks if the game is a draw (all cells on the board are filled).
* Returns True if it's a draw, False otherwise.

### if __name__ == "__main__": block:
* Executes the game by calling the startPlayingGame function when the script is run.

In summary, the code provides a playable Tic Tac Toe game where the player competes against an AI agent using the Min-Max algorithm to make optimal moves. The game continues until there is a winner or a draw.

## Code Execution
> python3 MiniMax.py

# Alpha-beta Pruning
Alpha-beta pruning is an optimization technique used in the Minimax algorithm to reduce the number of nodes evaluated in the search tree. This helps improve the efficiency of the algorithm by eliminating branches that are guaranteed to be irrelevant to the final decision. Alpha-beta pruning is particularly useful in games like tic-tac-toe, where the game tree can become quite large.

## Here's a simplified explanation of how alpha-beta pruning works in the context of tic-tac-toe:

### Alpha and Beta Values:
* In addition to the Minimax algorithm's basic structure, two values, alpha and beta, are maintained. They represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of, respectively.
* Initially, alpha is set to negative infinity, and beta is set to positive infinity.

### Pruning Conditions:
* During the recursive search of the game tree, if the current player (maximizing or minimizing) finds a move that is guaranteed to be worse than the current best move, it can stop evaluating further nodes in that branch. This is where the pruning occurs.
* If, at any point, the current player's score is greater than or equal to beta (for the maximizing player) or less than or equal to alpha (for the minimizing player), further exploration of that branch is unnecessary.

### Update Alpha and Beta:
* As the algorithm progresses, alpha and beta are updated accordingly. For the maximizing player, alpha is updated to the maximum of its current value and the newly found score. For the minimizing player, beta is updated to the minimum of its current value and the newly found score.

### Efficiency Improvement:
* By pruning branches that are guaranteed to be suboptimal, the search space is significantly reduced, leading to a more efficient algorithm.
* Alpha-beta pruning has a time complexity that is considerably better than the simple Minimax algorithm, especially when the game tree is large.

## Here's a high-level overview of the alpha-beta pruning process:

### Maximizing Player's Turn:
* If the current move's score is greater than or equal to beta, stop searching in this branch.
* Update alpha to be the maximum of its current value and the current move's score.

### Minimizing Player's Turn:
* If the current move's score is less than or equal to alpha, stop searching in this branch.
* Update beta to be the minimum of its current value and the current move's score.

### Repeat:
* Continue the process, exploring the game tree and updating alpha and beta until a terminal state is reached.

Alpha-beta pruning significantly reduces the number of nodes evaluated while preserving the minimax algorithm's ability to find the optimal move. In tic-tac-toe and similar games, this can lead to substantial computational savings.

## Code Explanation

### startPlayingGame() Function:
* Initializes an empty Tic Tac Toe grid with 9 spaces represented by a list.
* Alternates turns between the player and the AI until there is a winner or a draw.
* Calls drawGrid() to display the current state of the grid.
* Checks for a winner or a draw using the checkWinner() and checkDraw() functions.

### drawGrid(grid) Function:
* Takes the current state of the grid and prints it in the Tic Tac Toe board format.

### getPlayersMove(grid) Function:
* Prompts the player to enter a move (a number between 1 and 9).
* Checks if the input is valid (a digit between 1 and 9, and the chosen cell is not already filled).
* Returns the player's move.

### getAgentsMove(grid) Function:
* Calls the alphabeta() function to get the AI agent's move.
* Returns the move chosen by the AI.

### alphabeta(grid, isMaximizing, alpha, beta) Function:
* Implements the Alpha-Beta Pruning algorithm to determine the optimal move for the AI agent.
* Recursively evaluates possible moves, assigning scores based on the outcome of the game.
* Keeps track of alpha and beta values to prune branches that cannot affect the final decision.
* Returns the score and the corresponding move.

### checkWinner(grid) Function:
* Checks the grid for a winning combination by iterating through possible winning moves.
* Returns True if there is a winner, otherwise False.

### checkDraw(grid) Function:
* Checks if the grid is completely filled, indicating a draw.
* Returns True if there is a draw, otherwise False.

### if __name__ == "__main__": block:
* Calls the startPlayingGame() function to begin the game when the script is run.

In summary, this code provides a functional Tic Tac Toe game where a player can compete against an AI agent using the Alpha-Beta Pruning algorithm to make intelligent moves. The game continues until there is a winner or a draw.

## Code Execution
> python3 AlphaBeta.py

# Q-learning
Q-learning can be applied to tic-tac-toe as a way to create an agent that learns to play the game through trial and error. Q-learning is a model-free reinforcement learning algorithm that learns a policy for making decisions in an environment by iteratively updating its Q-values based on the observed rewards.

### Here's a step-by-step explanation of applying Q-learning to tic-tac-toe:

### State Representation:
* Define a representation for the current state of the tic-tac-toe board. This representation should be unique for each possible board configuration.

### Action Representation:
* Define the possible actions an agent can take in a given state. In tic-tac-toe, an action corresponds to placing an "X" or "O" in a particular empty cell.

### Q-Table Initialization:
* Create a Q-table to store the Q-values for each state-action pair. Initially, the Q-values are often set to zero.

### Exploration-Exploitation:
* During training, the agent needs to explore the environment to discover optimal strategies. The agent chooses actions with a balance between exploration and exploitation. This can be achieved using an epsilon-greedy strategy, where the agent explores with probability epsilon and exploits with probability 1 - epsilon.

### Reward Definition:
* Define the rewards for different outcomes. For tic-tac-toe, a positive reward can be given for winning, a negative reward for losing, and a small reward or zero for a draw.

### Q-Value Update:
* After taking an action and receiving a reward, update the Q-value for the state-action pair using the Q-learning update rule:

```
    Q(s,a)=Q(s,a)+α⋅[R+γ⋅maxa′​Q(s′,a′)−Q(s,a)]

        • Q(s,a) is the current Q-value for the state-action pair.
        • α is the learning rate.
        • R is the received reward.
        • γ is the discount factor.
        • s′ is the next state after taking action a.
```

### Training Episodes:
* Repeat the training process for a certain number of episodes or until convergence. During each episode, the agent plays tic-tac-toe, updates its Q-values based on the rewards received, and refines its strategy.

### Policy Extraction:
* After training, the agent's policy can be extracted from the learned Q-values. The agent chooses actions in a state based on the action with the highest Q-value.

### Testing:
* Evaluate the agent's performance by letting it play tic-tac-toe using its learned policy.

Q-learning allows the agent to gradually learn an optimal strategy for playing tic-tac-toe by interacting with the environment, receiving feedback in the form of rewards, and updating its Q-values accordingly. Over time, the agent should converge to a strategy that maximizes its expected cumulative reward in the game.

## Code Explanation

### initialization:
* Q: A dictionary to store Q-values for state-action pairs.
* alpha: Learning rate.
* gamma: Discount factor.
* epsilon: Exploration probability for the epsilon-greedy policy.
* stateSpace: Represents the game board with a 3x3 grid.
* actionSpace: Represents all possible actions (row, column) in the game.

### reward(state) Function:
* The reward function evaluates the current state and returns:
    - 1 if the player wins.
    - -1 if the agent wins.
    - 0 if the game is ongoing.

### epsilonGreedyPolicy(state, epsilon) Function:
* The epsilonGreedyPolicy function implements an epsilon-greedy policy for action selection.
* With probability epsilon, it selects a random action; otherwise, it chooses the action with the highest Q-value.
* Handles cases where multiple actions have the same maximum Q-value.

### qLearning(state, action, nextState, reward, alpha, gamma) Function:
* The qLearning function updates Q-values based on the Q-learning formula.
* state and nextState are converted to tuples to use them as keys in the Q dictionary.
* The Q-value for the current state-action pair is updated based on the immediate reward and the maximum Q-value of the next state.

### game initialization and loop:
* The game is initialized with an empty board (stateSpace).
* The game alternates between the player's turn and the agent's turn.
* The player and agent make moves based on input and the epsilon-greedy policy.
* The game loop breaks when there is a winner or a tie.

### updating Q-Values:
* After the game loop, the Q-values are updated using the qLearning function with the final state, action, reward, and hyperparameters.

In summary, this code sets up a Q-learning framework for a Tic Tac Toe game. It uses the Q-learning algorithm to update Q-values based on the rewards obtained during the game. The player and agent take turns making moves, and the Q-values are updated to improve the agent's strategy over time.

## Code Execution
> python3 QLearning.py