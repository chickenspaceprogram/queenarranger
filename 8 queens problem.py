import numpy
def board_valid(row: int, col: int):
    '''
    Returns whether the board inputted is valid if a queen is added to the space given by row, col. 
    '''
    global board
    global board_size
    if (1 in board[row]) or (1 in board[:, col]) or (1 in numpy.diagonal(board, offset=(col - row))) or (1 in numpy.rot90(board).diagonal(offset=(row + col - board_size + 1))):
        return False
    return True

def print_board(board: numpy.ndarray):
    '''
    Prints board formatted nicely as well as num_boards.
    '''
    global num_boards
    num_boards += 1
    boardaslist = board.tolist()
    global board_size
    print()
    print(f"Board {num_boards}")
    for row in range(board_size):
        disp_string = ''
        print('|' + '---|' * board_size)
        for col in range(board_size):
            if boardaslist[row][col] == 1:
                disp_string = f'{disp_string}| Q '
            else:
                disp_string = f'{disp_string}|   '
        print(disp_string + '|')
    print('|' + '---|' * board_size)

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

def recursive_solver(initrow: int):
    '''
    A recursive function that solves stuff using backtracking.
    '''
    global board
    global num_queens
    global num_boards
    global boards_list
    global board_size
    for col in range(board_size):
        if board_valid(initrow, col):
            board[initrow, col] = 1
            if initrow >= (board_size - 1):
                boards_list.append(board.copy())
                board[initrow, col] = 0
                return
            recursive_solver(initrow + 1)
            board[initrow, col] = 0

num_queens = 0
num_boards = 0
boards_list = []
board_size = int(input("Please enter desired board size: "))
board = numpy.zeros((board_size, board_size))
recursive_solver(0)

lenboardslist = len(boards_list)

if lenboardslist == 0:
    print("No boards found.")

for i in range(lenboardslist):
    board_check = boards_list.pop(0)
    if is_new_board(board_check):
        print_board(board_check)