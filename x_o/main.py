from funcs import *
import cfg

def main():
    info()
    # fishki(cfg.X, cfg.O)
    board = new_board(9, cfg.EMPTY_BOARD_FIELD)
    print_board(board)

if __name__ == '__main__':
    main()