import numpy
def board_valid(row: int, col: int):
    '''
    Returns whether the board inputted is valid if a queen is added to the space given by row, col. 
    '''
    global board
    if (1 in board[row]) or (1 in board[:, col]) or (1 in numpy.diagonal(board, offset=(col - row))) or (1 in numpy.rot90(board).diagonal(offset=(row + col - 7))):
        return False
    return True

board = numpy.zeros((8, 8))
num_queens = 0
pastnumqueens = 0

def print_board():
    global board
    boardlist = board.tolist()
    for row in range(8):
        disp_string = ''
        for col in range(8):
            if boardlist[row][col] == 1:
                disp_string = f'{disp_string} Q'
            else:
                disp_string = f'{disp_string} ·'
        print(disp_string)

def recursive_solver():
    '''
    A recursive function that solves stuff using backtracking.
    '''
    global board
    global num_queens
    for row in range(0, 8):
        for col in range(0, 8):
            if board_valid(row, col):
                board[row, col] = 1
                num_queens += 1
                recursive_solver()
                if num_queens == 8:
                    return
                board[row, col] = 0
                num_queens -= 1


recursive_solver()

print_board()