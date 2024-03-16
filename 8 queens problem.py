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
num_boards = 0

def print_board():
    global board
    global num_boards
    boardlist = board.tolist()
    print()
    num_boards += 1
    for row in range(8):
        disp_string = ''
        for col in range(8):
            if boardlist[row][col] == 1:
                disp_string = f'{disp_string} Q'
            else:
                disp_string = f'{disp_string} ·'
        print(disp_string)
    print(num_boards)

def recursive_solver(initrow: int):
    '''
    A recursive function that solves stuff using backtracking.
    '''
    global board
    global num_queens
    for col in range(8):
        if board_valid(initrow, col):
            board[initrow, col] = 1
            if initrow >= 7:
                print_board()
                board[initrow, col] = 0
                return
            recursive_solver(initrow + 1)
            board[initrow, col] = 0

recursive_solver(0)