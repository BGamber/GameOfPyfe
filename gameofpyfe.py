## Conway's Game of Life, in Python
## Ben Gamber
## Any live cell with less than two live neighbours dies.
## Any live cell with two or three live neighbours remains living.
## Any live cell with more than three live neighbours dies.
## Any dead cell with exactly three live neighbours becomes a live cell.
## A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

import os, time

def print_board(board):
    # os.system('clear')
    for row in board:
        print ' '.join(row)

def test_cell(board, x, y):
    live_neighbors = 0
    this_cell = board[y][x]
    for row_mod in range(-1,2):
        for col_mod in range(-1,2):
            if x + col_mod < 20 and y + row_mod < 20:
                if board[y+row_mod][x+col_mod] == 'o' and \
                (col_mod != 0 and row_mod != 0): ## TODO: This is breaking
                    live_neighbors += 1
    if this_cell == 'o':
        if live_neighbors < 2 or live_neighbors > 3:
            return False
        elif live_neighbors == 2 or live_neighbors == 3:
            return True
    elif this_cell == 'x':
        if live_neighbors == 3:
            return True
        else:
            return False

count = 0
board = []
for i in range(20):
    board.append(['x']*20)

board[2][3] = 'o'
board[3][3] = 'o'
board[4][3] = 'o'
print_board(board)

assert test_cell(board, 2, 3) == True, 'Dead cell with 3 neighbors should be True'
assert test_cell(board, 3, 3) == True, 'Live cell with 2 neighbors should be True'
assert test_cell(board, 3, 2) == False, 'Live cell with 1 neighbor should be False'

while True:
    new_board = []
    for row in range(20):
        new_board.append([])
        for column in range(20):
            new_board[row].append([])
            print column,row,test_cell(board, column, row)
            if test_cell(board, column, row):
                new_board[row][column] = 'o'
            else:
                new_board[row][column] = 'x'
    print_board(new_board)
    board = new_board
    print_board(board)
    time.sleep(1)