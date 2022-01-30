#File Info:
#Created: 2020-01-29
#Author: Adrian Schauer
#Description: This file contains the class Board.
# . stands for empty field on the board.
# X stands for a hit on the board.
# O stands for a miss on the board.

from shiptype import ShipType
from ship import Ship


class Board:
    def __init__(self):
        "This function initializes the board."
        self.board = [10 * ['.'] for i in range(10)]
        self.ships_placed = 0
        self.ships_sunk = 0
        self.ships = [Ship(ShipType.AircraftCarrier), Ship(ShipType.Battleship), Ship(ShipType.Submarine), Ship(ShipType.Destroyer), Ship(ShipType.PatrolBoat)]
    
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

    def place_ship(self, ship, x, y, rotation):
        "This function places a ship on the board."
        #check if ship can be placed
        if self.check_ship_placement(ship, x, y, rotation):
            #place ship
            for i in range(ship.getLength()):
                if rotation == Ship.Rotation.H:
                    self.board[y][x + i] = ship.getSymbol()
                else:
                    self.board[y + i][x] = ship.getSymbol()
            #increase number of ships placed
            self.ships_placed += 1
            return True
        else:
            return False

    def check_ship_placement(self, ship, x, y, rotation):
        "This function checks if a ship can be placed."
        #check if ship can be placed
        if rotation == Ship.Rotation.H:
            if x + ship.getLength() > 10:
                return False
            for i in range(ship.getLength()):
                if self.board[y][x + i] != '.':
                    return False
        else:
            if y + ship.getLength() > 10:
                return False
            for i in range(ship.getLength()):
                if self.board[y + i][x] != '.':
                    return False
        return True
