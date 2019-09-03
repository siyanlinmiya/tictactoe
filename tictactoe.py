import random

def drawBoard(board):
    # This function prints out the board that it was passed.
    # Print out the board that it was passed
    print('-----------------------------')
    print(
        ' ' + board[36] + ' | ' + board[37] + ' | ' + board[38] + ' | ' + board[39] + ' | ' + board[40] + ' | ' + board[
            41] + ' | ' + board[42])
    print(
        ' ' + board[29] + ' | ' + board[30] + ' | ' + board[31] + ' | ' + board[32] + ' | ' + board[33] + ' | ' + board[
            34] + ' | ' + board[35])
    print(
        ' ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25] + ' | ' + board[26] + ' | ' + board[
            27] + ' | ' + board[28])
    print(
        ' ' + board[15] + ' | ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[
            20] + ' | ' + board[21])
    print(' ' + board[8] + ' | ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12] + ' | ' + board[
        13] + ' | ' + board[14])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' + board[
        6] + ' | ' + board[7])
    print('-----------------------------')
    print(' ' + str(1) + ' | ' + str(2) + ' | ' + str(3) + ' | ' + str(4) + ' | ' + str(5) + ' | ' + str(6) + ' | ' + str(7))


def inputPlayerLetter():
    # Lets th player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = raw_input().upper()
            # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Computer first'

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getMovelist(board):
    movelist = []
    for i in range(1, 8):
        for j in range(0, 6):
            position = i + j * 7
            if isSpaceFree(board, position):
                movelist.append(position)
                break
    return movelist

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
#    while move not in getMovelist(board) or not isSpaceFree(board, int(move)):
    while move not in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42".split() or not isSpaceFree(board, int(move)):
        print('What is your next move?')
        print(getMovelist(board))
        move = raw_input()
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter

isWinnerList = []
def isWinner(bo, le):
    for j in range(1, 7):
        for i in range((j - 1) * 7 + 1, (j - 1) * 7 + 5):
            if bo[i] == bo[i + 1] == bo[i + 2] == bo[i + 3] == le:
                return (le + ' ' + 'Win')
                isWinnerList = []
                break

    for j in range(1, 8):
        for i in range(0, 3):
            if bo[j+i*7] == bo[j + (i+1) * 7] == bo[j + (i+2) * 7] == bo[j + (i+3) * 7] == le:
                return (le + ' ' + 'Win')
                break

    for i in range(0, 3):
        for j in range(1 + i * 7, 5 + i * 7):
            if bo[j] == bo[1 + j + 1 * 7] == bo[2 + j + 2 * 7] == bo[3 + j + 3 * 7] == le:
                return (le + ' ' + 'Win')
                break
            elif bo[j + 3 * 7] == bo[ 1 + j + 2 * 7] == bo[2 + j + 1 * 7] == bo[3 + j] == le:
                return (le + ' ' + 'Win')
                break

## new strategy level2 machine
isalmostWinnerList = []
def isalmostWinner(bo, le):
    for j in range(1, 7):
        for i in range((j - 1) * 7 + 1, (j - 1) * 7 + 6):
            if bo[i] == bo[i + 1] == bo[i + 2] == le:
                return (le + ' ' + 'AlmostWin')
                isalmostWinnerList = []
                break10

    for j in range(1, 8):
        for i in range(0, 4):
            if bo[j+i*7] == bo[j + (i+1) * 7] == bo[j + (i+2) * 7] == le:
                return (le + ' ' + 'AlmostWin')
                break

    for i in range(0, 3):
        for j in range(1 + i * 7, 6 + i * 7):
            if bo[j] == bo[1 + j + 1 * 7] == bo[2 + j + 2 * 7] == le:
                return (le + ' ' + 'AlmostWin')
                break
            elif bo[j + 3 * 7] == bo[ 1 + j + 2 * 7] == bo[2 + j + 1 * 7] == le:
                return (le + ' ' + 'AlmostWin')
                break
  ########


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def chooseRandomMoveFromList(board, moveList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    computerMove = 0
    movelist = getMovelist(board)
    for i in range(1, 43):
        copy = getBoardCopy(board)
        if i in movelist and isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                computerMove = i
                break

    if computerMove == 0:
        # Check if the player could win on their next move, and block them.
        for i in range(1, 43):
            copy = getBoardCopy(board)
            if  i in movelist and isSpaceFree(copy, i):
                makeMove(copy, playLetter, i)
                if isWinner(copy, playLetter):
                    computerMove = i
                    break

                elif isalmostWinner(copy, playLetter):  ## level2 strategy improve
                    computerMove = i
                    break
#                elif isRightCloseWinner(copy, playLetter):
#                    computerMove = i
#                    break

    if computerMove == 0:
        computerMove = chooseRandomMoveFromList(board, movelist)

    return computerMove

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 43):
        if isSpaceFree(board, i):
            return False
    return True

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


###_________________________GAME START______________________________________
use = inputPlayerLetter()
playLetter = use[0]
computerLetter = use[1]

while True:
    tactoe = [' '] * 43
    drawBoard(tactoe)
    if random.randint(0, 1) == 0:
        print('Computer first')
        for i in range(1, 21):
            computerMove = getComputerMove(tactoe, computerLetter)
            makeMove(tactoe, computerLetter, computerMove)
            drawBoard(tactoe)
            if isWinner(tactoe, computerLetter):
                print(isWinner(tactoe, computerLetter))
                break
            playMove = getPlayerMove(tactoe)
            makeMove(tactoe, playLetter, playMove)
            drawBoard(tactoe)
            if isWinner(tactoe, playLetter):
                print(isWinner(tactoe, playLetter))
                break
    else:
        print('Player first')
        for i in range(1, 21):
            playMove = getPlayerMove(tactoe)
            makeMove(tactoe, playLetter, playMove)
            drawBoard(tactoe)
            if isWinner(tactoe, playLetter):
                print(isWinner(tactoe, playLetter))
                break
            computerMove = getComputerMove(tactoe, computerLetter)
            makeMove(tactoe, computerLetter, computerMove)
            drawBoard(tactoe)
            if isWinner(tactoe, computerLetter):
                print(isWinner(tactoe, computerLetter))
                break
    if not playAgain():
        break

