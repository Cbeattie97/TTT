board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentPlayer = "X"
winner = None
gameIsRunning = True


# printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take plaayer input
def playerInput(board):
    inp = int(input("Enter the position from 1-9: "))
    if inp >= 1 and inp <= 9:
        if board[inp-1] == "_":
            board[inp-1] = currentPlayer
        else:
            print("Position already taken")
            playerInput(board)

# check for win or tie
def checkWin(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        print ("Player " + winner + " Wins!!")
    if board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        print ("Player " + winner + " Wins!!")
    if board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        print ("Player " + winner + " Wins!!")
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        print ("Player " + winner + " Wins!!")
    if board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        print ("Player " + winner + " Wins!!")
    if board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        print ("Player " + winner + " Wins!!")
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        print ("Player " + winner + " Wins!!")
    if board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        print ("Player " + winner + " Wins!!")
    if "_" not in board:
        print("The Game is a Tie!")

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#  check for win or tie again 
while gameIsRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    if winner != None:
        printBoard(board)
        gameIsRunning = False
    switchPlayer()