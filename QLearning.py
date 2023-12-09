import numpy as np
import random

# Initializing Q-values
Q = {}

# Hyperparameters - learning rate, discount factor, exploration probability
alpha = 0.1 
gamma = 0.9 
epsilon = 0.1 

# game state and action space
stateSpace = [[0, 0, 0] for i in range(3)]
actionSpace = [(i, j) for i in range(3) for j in range(3)]

# reward function - check rows, columns, diagnols
def reward(state):
    if any(sum(row) == 3 for row in state): 
        return 1
    if any(sum(column) == 3 for column in zip(*state)): 
        return 1
    if sum(state[i][i] for i in range(3)) == 3: 
        return 1
    if sum(state[i][2-i] for i in range(3)) == 3:
        return 1
    if any(sum(row) == -3 for row in state): 
        return -1
    if any(sum(column) == -3 for column in zip(*state)):
        return -1
    if sum(state[i][i] for i in range(3)) == -3: 
        return -1
    if sum(state[i][2-i] for i in range(3)) == -3: 
        return -1
    return 0

# epsilon-greedy policy
def epsilonGreedyPolicy(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actionSpace)
    else:
        qValues = [Q.get((tuple(map(tuple, state)), action), 0) for action in actionSpace]
        maxQValue = max(qValues)
        count = qValues.count(maxQValue)
        if count > 1:
            bestActions = [actionSpace[i] for i in range(len(actionSpace)) if qValues[i] == maxQValue]
            return random.choice(bestActions)
        else:
            return actionSpace[qValues.index(maxQValue)]
    
# Q-learning algorithm
def qLearning(state, action, nextState, reward, alpha, gamma):
    state = tuple(map(tuple, state))
    nextState = tuple(map(tuple, nextState))
    # Geting Q-value for current state-action pair
    qValue = Q.get((state, action), 0)
    # Calculating the maximum Q-value for the next state
    maxQValue = max([Q.get((nextState, a), 0) for a in actionSpace])
    # Updating the Q-value using Q-learning formula
    Q[tuple(map(tuple, state)), action] = qValue + alpha * (reward + gamma * maxQValue - qValue)

# Initializing the game
state = stateSpace.copy()
while True:
    # our turn
    print("Current state is ")
    print(np.array(state))
    row = int(input("Please enter a row between 0-2: "))
    column = int(input("Please enter a column between 0-2: "))
    if state[row][column] != 0:
        print("Invalid")
        continue
    state[row][column] = 1
    rewardValue = reward(state)
    if rewardValue != 0:
        print("You won!")
        break
    if all(all(row) for row in state):
        print("Tie!")
        break
    # agent's turn
    action = epsilonGreedyPolicy(state, epsilon)
    state[action[0]][action[1]] = -1
    rewardValue = reward(state)
    if rewardValue != 0:
        print("You lost!")
        break
    if all(all(row) for row in state):
        print("Tie!")
        break

# Updating Q-values
qLearning(state, action, state, rewardValue, alpha, gamma)