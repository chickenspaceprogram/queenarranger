import numpy
def board_valid(row: int, col: int):
    '''
    Returns whether the board inputted is valid if a queen is added to the space given by row, col. 
    '''
    global board
    if 1 in board[row] or 1 in board[:][col] or 1 in numpy.diag(board, k=(row - col)):
        return False
    return True

board = numpy.zeros((8, 8))
num_queens = 0

def recursive_solver(loc: int):
    '''
    A recursive function that solves stuff using backtracking.
    '''
    global board
    global num_queens
    rowstart = loc // 8
    colstart = loc % 8
    for row in range(rowstart, 8):
        for col in range(colstart, 8):
            if board_valid(row, col):
                board[row][col] = 1
                num_queens += 1
                if num_queens == 8:
                    print(board)
                    quit()
                recursive_solver((row * 8 + col))
                board[row][col] = 0
                num_queens -= 1


recursive_solver(0)