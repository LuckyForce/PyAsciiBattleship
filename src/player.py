#File Info:
#Created: 2020-01-29
#Author: Adrian Schauer
#Description: This file contains class for player

from PyAsciiBattleship.src.board import Board
from PyAsciiBattleship.src.ship import Ship


class Player:
    def __init__(self):
        self.moves = 0
        self.ships = []
        self.board = Board()
