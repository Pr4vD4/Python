EMPTY_BOARD_FIELD = '-'
X = 'X'
O = 'O'

TIE = 'None is a winner'

wins = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)
comp_wins = (
    4, 0, 2, 6, 8, 1, 3, 5, 7
)
