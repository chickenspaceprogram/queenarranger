import numpy
def board_valid(row: int, col: int):
    '''
    Returns whether the board inputted is valid if a queen is added to the space given by row, col. 
    '''
    global board
    if (1 in board[row]) or (1 in board[:, col]) or (1 in numpy.diagonal(board, offset=(col - row))) or (1 in numpy.rot90(board).diagonal(offset=(row + col - 7))):
        return False
    return True

def print_board(board: numpy.ndarray):
    '''
    Prints board formatted nicely as well as num_boards.
    '''
    global num_boards
    num_boards += 1
    boardaslist = board.tolist()
    print()
    for row in range(8):
        disp_string = ''
        for col in range(8):
            if boardaslist[row][col] == 1:
                disp_string = f'{disp_string} Q'
            else:
                disp_string = f'{disp_string} ·'
        print(disp_string)
    print(num_boards)

def is_new_board(board: numpy.ndarray):
    '''
    Finds all permutations of board, then checks to see if any of them are in boards_list.
    '''
    global boards_list
    all_board_permuts = []
    for i in range(4):
        all_board_permuts.append(numpy.rot90(board, k=i))
        all_board_permuts.append(numpy.transpose(numpy.rot90(board, k=i)))
    for j in all_board_permuts:
        for k in boards_list:
            if numpy.array_equal(j, k):
                return False
    return True


board = numpy.zeros((8, 8))
num_queens = 0
num_boards = 0
boards_list = []

def recursive_solver(initrow: int):
    '''
    A recursive function that solves stuff using backtracking.
    '''
    global board
    global num_queens
    global num_boards
    global boards_list
    for col in range(8):
        if board_valid(initrow, col):
            board[initrow, col] = 1
            if initrow >= 7:
                boards_list.append(board.copy())
                board[initrow, col] = 0
                return
            recursive_solver(initrow + 1)
            board[initrow, col] = 0

recursive_solver(0)
lenboardslist = len(boards_list)

for i in range(lenboardslist):
    board_check = boards_list.pop(0)
    if is_new_board(board_check):
        print_board(board_check)