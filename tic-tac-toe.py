#e01a01c01
#tic-tac-toe oyunu
import random

def display_board(board):
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Hamleni yap (1-9): "))

            if not (1 <= move <= 9):
                print("Lütfen 1-9 arasında bir sayı girin.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("Bu kare dolu.")

        except ValueError:
            print("Lütfen bir sayı girin.")

def get_free_squares(board):
    free_squares = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_squares.append((r, c))
    return free_squares

def check_win(board, mark):
    for r in range(3):
        if board[r][0] == mark and board[r][1] == mark and board[r][2] == mark:
            return True

    for c in range(3):
        if board[0][c] == mark and board[1][c] == mark and board[2][c] == mark:
            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True

    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False

def computer_move(board):
    free_squares = get_free_squares(board)
    
    if free_squares:
        index = random.randrange(len(free_squares))
        row, col = free_squares[index]
        board[row][col] = 'X'

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

board[1][1] = 'X'
print("Bilgisayar ilk hamlesini yaptı.")
display_board(board)

while True:
    enter_move(board)
    display_board(board)

    if check_win(board, 'O'):
        print("Kazandın!")
        break

    if not get_free_squares(board):
        print("Berabere!")
        break

    computer_move(board)
    display_board(board)

    if check_win(board, 'X'):
        print("Bilgisayar kazandı!")
        break

    if not get_free_squares(board):
        print("Berabere!")
        break
