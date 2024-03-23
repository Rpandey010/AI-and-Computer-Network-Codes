# I assume the role of player 'o'
# while winning is not guaranteed, my responsibility is to make the best move possible
# and yes we can always try again, its a game after all

import random

def pboard(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def checkwinner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # checkingg diag
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def bestmove(board):
    # Rule (a) and (b) 
    # Being a player 'o', if in a row/column/diagonal has 2 consecutive 'x' i will put 'o' at blank space 
    # Also if in a row/column/diagonal has 2 consecutive '0', i will put 'o' at blank space and win
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Checkingg rows and columns for consecutive x or o
                if (board[i].count('x') == 2 and board[i].count('o') == 0) or \
                   (board[j].count('x') == 2 and board[j].count('o') == 0):
                    return i, j

                # Checkingg diagonals for consecutive x or o
                if i == j and board[i][i].count('x') == 2 and board[i][i].count('o') == 0:
                    return i, i
                if i + j == 2 and board[i][2 - i].count('x') == 2 and board[i][2 - i].count('o') == 0:
                    return i, 2 - i

    # Rule (c) and (d)
    # If a row/column/diagonal has 1 'x' or 'o', i will put 'o' at any one blank space out of two
    # We are not gonna win through this move but its the best move to do
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                if board[i].count('x') == 1 and board[i].count('o') == 0:
                    return i, j
                if board[j].count('x') == 1 and board[j].count('o') == 0:
                    return j, i
                if i == j and board[i][i].count('x') == 1 and board[i][i].count('o') == 0:
                    return i, i
                if i + j == 2 and board[i][2 - i].count('x') == 1 and board[i][2 - i].count('o') == 0:
                    return i, 2 - i

    # Rule (e)
    blanks = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(blanks)

# Game loop
while True:
    # Blank board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Player 'x' and 'o' moves
    while True:
        pboard(board)

        # 'x' Player turn 
        row, col = bestmove(board)
        board[row][col] = 'x'
        print("\n")  

        # Checkingg if 'x' wins
        if checkwinner(board, 'x'):
            pboard(board)
            print("Player 'x' wins!")
            break

        # Is it a tie?
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            pboard(board)
            print("TIEEE!")
            break

        # 'o' Player turn 
        row, col = bestmove(board)
        board[row][col] = 'o'
        print("\n")  

        # Checkingg if 'o' wins
        if checkwinner(board, 'o'):
            pboard(board)
            print("Player 'o' wins!")
            break

    playagain = input("Lost?? TRYY AGAINNN! (yes/no): ").lower()
    if playagain != 'yes':
        break
