def startPlayingGame():
    grid = [" " for _ in range(9)]
    playerTurn = True
    print("Hello, You are about to play Tic Tac Toe game against an AI agent based on Min-Max Algorithm. Good luck!!")
    drawGrid(grid)
    while True:
        if playerTurn:
            move = getPlayersMove(grid)
            grid[move] = "X"
        else:
            print("Agent's turn")
            move = getAgentsMove(grid)
            grid[move] = "O"
        drawGrid(grid)
        if checkWinner(grid):
            if playerTurn:
                print("Congratulations! You won the game.")
            else:
                print("Oh no! Agent won the game. Good luck next time")
            break
        elif checkDraw(grid):
            print("No moves left! It's a draw.")
            break
        playerTurn = not playerTurn

def drawGrid(grid):
    print(grid[0], "|", grid[1], "|", grid[2])
    print("---------")
    print(grid[3], "|", grid[4], "|", grid[5])
    print("---------")
    print(grid[6], "|", grid[7], "|", grid[8])

def getPlayersMove(grid):
    isValidMove = False
    while not isValidMove:
        move = input("Your turn. Please enter a move between 1-9: ")
        if move.isdigit() and int(move) in range(10) and grid[int(move) - 1] == " ":
            return int(move) - 1
        else:
            print("Invalid move")

def getAgentsMove(grid):
    bestScore = -float("inf")
    bestMove = None
    for i in range(9):
        if grid[i] == " ":
            grid[i] = "O"
            score = miniMax(grid, False)
            grid[i] = " "
            if score > bestScore:
                bestScore = score
                bestMove = i
    return bestMove

def miniMax(grid, isMaximizing):
    if checkWinner(grid):
        if isMaximizing:
            return -1
        else:
            return 1
    elif checkDraw(grid):
        return 0
    elif isMaximizing:
        bestScore = -float("inf")
        for i in range(9):
            if grid[i] == " ":
                grid[i] = "O"
                score = miniMax(grid, False)
                grid[i] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        leastScore = float("inf")
        for i in range(9):
            if grid[i] == " ":
                grid[i] = "X"
                score = miniMax(grid, True)
                grid[i] = " "
                if score < leastScore:
                    leastScore = score
        return leastScore

def checkWinner(grid):
    winningMoves = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for x, y, z in winningMoves:
        if grid[x] == grid[y] == grid[z] != " ":
            return True
    return False

def checkDraw(grid):
    return " " not in grid

if __name__ == "__main__":
    startPlayingGame()