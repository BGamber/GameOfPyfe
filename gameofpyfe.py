## Conway's Game of Life, in Python
## Ben Gamber
## Any live cell with less than two live neighbours dies.
## Any live cell with two or three live neighbours remains living.
## Any live cell with more than three live neighbours dies.
## Any dead cell with exactly three live neighbours becomes a live cell.
## A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

import os, time

def print_board(board):
    os.system('clear')
    for row in board:
        print ' '.join(row)

def test_cell(board, x, y, size):
    live_neighbors = 0
    this_cell = board[y][x]
    for row_mod in range(-1,2):
        for col_mod in range(-1,2):
            if x + col_mod >= 0 and x + col_mod < size and \
            y + row_mod >= 0 and y + row_mod < size:
                if board[y+row_mod][x+col_mod] == '*' and \
                not (col_mod == 0 and row_mod == 0):
                    live_neighbors += 1
    if this_cell == '*':
        if live_neighbors < 2 or live_neighbors > 3:
            return False
        elif live_neighbors == 2 or live_neighbors == 3:
            return True
    elif this_cell == '.':
        if live_neighbors == 3:
            return True
        else:
            return False

size = 52
count = 0
board = []
for i in range(size):
    board.append(['.']*size)

board[26][26] = '*'
board[26][27] = '*'
board[27][25] = '*'
board[27][26] = '*'
board[28][26] = '*'
print_board(board)

# assert test_cell(board, 2, 3) == True, 'Dead cell with 3 neighbors should be True'
# assert test_cell(board, 3, 3) == True, 'Live cell with 2 neighbors should be True'
# assert test_cell(board, 3, 2) == False, 'Live cell with 1 neighbor should be False'

while True:
    new_board = []
    for row in range(size):
        new_board.append([])
        for column in range(size):
            new_board[row].append([])
            if test_cell(board, column, row, size):
                new_board[row][column] = '*'
            else:
                new_board[row][column] = '.'
    print_board(new_board)
    if new_board == board:
        print 'Simulation stabilized.'
        break
    else:
        board = new_board
        print_board(board)
        time.sleep(0.1)