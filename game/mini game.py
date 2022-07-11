theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []
already_picked = []
for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    """simply calls the board and displays it to the user."""
    print()
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('---+---+---')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('---+---+---')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print()


def game():
    """This is the minigame. It takes input from user (1-9) and adds an "X" in the corresponding spot.
    The "O" player is played by the computer and it will randomly pick a spot that is not taken.
    If user enters value that is not integer(1-9), function will ask user to enter a valid value.
    If value on board is taken, it will ask to enter a non-taken value.

    If either the player or computer reaches three-in-a-row, that user wins.
    If not, it ends in a tie."""

    global win
    turn = 'X'
    win = turn
    count = 0

    for i in range(10):
        printBoard(theBoard)
        try:
            if turn == 'X':
                print("It's your turn, " + turn + ". Move to which place? Pick number (1-9): ")
                move = input()
                already_picked.append(move)

            else:
                move = str(random.randrange(1, 10))
                already_picked.append(move)
                print('The computer chose the "', move, '" position.', sep="")

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Now we will check if player X or O has won,for every move after 5 moves.
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                    printBoard(theBoard)
                    print("Game Over.\n")
                    print(" **** " + turn + " won. ****")
                    win = turn
                    for key in board_keys:
                        theBoard[key] = " "
                    break

                    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("Game Over.\n")
                print("It's a Tie!!")
                for key in board_keys:
                    theBoard[key] = " "

            # Now we have to change the player after every move.
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        except:
            print("**ERROR. Please enter unoccupied spot with integer value (1-9):  ")
    for key in board_keys:
        theBoard[key] = " "
    if win == 'X':
        capture = 'T'
        return capture
    else:
        capture = 'F'
        return capture
