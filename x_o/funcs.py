# 1 - field 3x3
# 2 - print info
# 3 - choose the first turn
# 4 - result

wins_ = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)


def info():
    print("""
    Enter field position:

    0  |  1  |  2
    -------------
    3  |  4  |  5
    -------------
    6  |  7  |  8 

    """)


def ask(ask: str):
    answer = None
    while answer not in ('y', 'n'):
        answer = input(ask + 'y or n').lower()
    if answer == 'y':
        return True
    else:
        return False


def fishki(X: str = 'X', O: str = 'O'):
    first_turn = ask('Would you like to have a first turn?')
    if first_turn:
        print('You are - X')
        return O, X
    else:
        print('You are - O')
        return X, O


def turn_position(low: int, high: int):
    answer = int(input('Your turn position: '))
    if answer not in range(low, high):
        turn_position(low, high)
    else:
        return answer


def new_board(size: int, EMPTY_BOARD_FIELD: str = ' '):
    return [EMPTY_BOARD_FIELD for i in range(size)]


def print_board(board):
    print(" | ".join(board[:3]))
    print(" | ".join(board[3:6]))
    print(" | ".join(board[6:9]))


def legal_moves(board, EMPTY_BOARD_FIELD: str = '-'):
    legal_moves = []
    for i, pos in enumerate(board):
        if pos == EMPTY_BOARD_FIELD:
            legal_moves.append(i)
    return legal_moves


def winner(board: list, wins: tuple = wins_, EMPTY_BOARD_FIELD: str = '-', TIE: str = 'None is a winner'):
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != EMPTY_BOARD_FIELD:
            return board[win[0]]
        if EMPTY_BOARD_FIELD not in board:
            return TIE


def human_moves(board: list):
    legal_moves_l = legal_moves(board)
    move_position = turn_position(0, len(board))
    if move_position not in legal_moves_l:
        print('Your turn is no available')
        human_moves(board)
    return move_position


def comp_move(board: list, wins: tuple, wins_comp: tuple, comp_symbol: str, human_symbol: str,
              EMPTY_BOARD_FIELD: str = '-'):
    board = board.copy()
    print('Computer decides to go: ')
    for move in legal_moves(board):
        board[move] = comp_symbol
        if winner(board, wins) == human_symbol:
            print(move)
            return move
            board[move] = EMPTY_BOARD_FIELD
    for move in wins_comp:
        if move in legal_moves(board):
            print(move)
            return move
            board[move] = EMPTY_BOARD_FIELD
