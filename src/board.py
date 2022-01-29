#File Info:
#Created: 2020-01-29
#Author: Adrian Schauer
#Description: This file contains the class Board.
# . stands for empty field on the board.
# X stands for a hit on the board.
# O stands for a miss on the board.

class Board:
    def __init__(self):
        "This function initializes the board."
        self.board = [10 * ['.'] for i in range(10)]
    
    def print_board(self):
        "This function prints the board."
        #print board in following format:
        # - - - - - - - - - - - -
        # - - A B C D E F G H I -
        # - 1 X X X X X X X X X -
        # - 2 X X X X X X X X X -
        # - 3 X X X X X X X X X -
        # - 4 X X X X X X X X X -
        # - 5 X X X X X X X X X -
        # - 6 X X X X X X X X X -
        # - 7 X X X X X X X X X -
        # - 8 X X X X X X X X X -
        # - 9 X X X X X X X X X -
        print(' - - - - - - - - - - - - ')
        print(' - - A B C D E F G H I J - ')
        for i in range(10):
            print(' - ' + str(i + 1) + ' ' + ' '.join(self.board[i]))
        print(' - - - - - - - - - - - - ')
