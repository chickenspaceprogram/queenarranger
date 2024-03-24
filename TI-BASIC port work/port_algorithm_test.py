# Code here is very suboptimal for python. I swear I'm not dumb enough to code this willingly.
# Built this way to map easier onto TI-BASIC which only has global variables and has a few other quirks.


# ok, so I've abandoned this. Got fed up trying to convert between 0-index arrays (python) and 1-index arrays (TI-BASIC).
# Included in the GitHub repository because why not.

import numpy as np
board_size = int(input("Please enter desired board size: "))
board = np.zeros((board_size, board_size))
row_current = 0
col_current = 0
is_valid_return = True

def board_is_valid():  # Not using NumPy's inbuilt functions for checking diagonals, rows, and cols since those are not present in TI-BASIC
    global board
    global board_size
    global row_current
    global col_current
    global is_valid_return

    for i in range(board_size):
        if board[row_current, i] == 1 or board[i, col_current] == 1:
            is_valid_return == False
            return
    init_row = (row_current - col_current) * ((row_current - col_current) >= 0) # both of these statements would have a +1 at the end in ti basic
    init_col = col_current - row_current * ((row_current - col_current) < 0) # seriously why did at TI make lists start at 1, its annoying as hell
    for i in range(board_size - abs(row_current - col_current)):
        if board[init_row + i, init_col + i] == 1:
            is_valid_return = False
            return
    init_row = (row_current + col_current - 3) * ((row_current + col_current - 3) > board_size - 1) + (board_size - 1)(row_current + col_current - 3 <= board_size)