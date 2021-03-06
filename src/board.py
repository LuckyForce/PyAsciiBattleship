#File Info:
#Created: 2020-01-29
#Author: Adrian Schauer
#Description: This file contains the class Board.
# . stands for empty field on the board.
# X stands for a hit on the board.
# O stands for a miss on the board.

from shiprotation import ShipRotation
from shiptype import ShipType
from ship import Ship


class Board:
    def __init__(self):
        "This function initializes the board."
        self.board = [10 * ['.'] for i in range(10)]
        self.ship_board = [10 * ['.'] for i in range(10)]
        self.ships_placed = 0
        self.ships_sunk = 0
        self.ships = [Ship(ShipType.AircraftCarrier), Ship(ShipType.Battleship), Ship(ShipType.Submarine), Ship(ShipType.Destroyer), Ship(ShipType.PatrolBoat)]
    
    def check_win(self):
        "This function checks if every ship got hit."
        #check if every ship got hit
        if self.ships_sunk == len(self.ships):
            return True
        else:
            return False

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
            print(' - ' + str(i) + ' ' + ' '.join(self.board[i]))
        print(' - - - - - - - - - - - - ')

    def print_ship_placements(self):
        "This function prints the ship placements."
        #print ship placements in following format:
        # - - - - - - - - - - - -
        # - - A B C D E F G H I J -
        # - 1 X X X X X X X X X X -
        # - 2 X X X X X X X X X X -
        # - 3 X X X X X X X X X X -
        # - 4 X X X X X X X X X X -
        # - 5 X X X X X X X X X X -
        # - 6 X X X X X X X X X X -
        # - 7 X X X X X X X X X X -
        # - 8 X X X X X X X X X X -
        # - 9 X X X X X X X X X X -
        print(' - - - - - - - - - - - - ')
        print(' - - A B C D E F G H I J - ')
        for i in range(10):
            print(' - ' + str(i) + ' ' + ' '.join(self.ship_board[i]))
        print(' - - - - - - - - - - - - ')

    def place_ship(self, ship, x, y, rotation=ShipRotation.Horizontal):
        "This function places a ship on the board."
        #check if ship can be placed
        if self.check_ship_placement(ship, x, y, rotation):
            #place ship
            for i in range(ship.getLength()):
                if rotation == ShipRotation.Horizontal:
                    self.ship_board[y][x + i] = ship.getSymbol()
                    ship.setX(x + i)
                    ship.setY(y)
                else:
                    self.ship_board[y + i][x] = ship.getSymbol()
                    ship.setX(x)
                    ship.setY(y + i)
            #increase number of ships placed
            self.ships_placed += 1
            #set ship as placed
            ship.setPlaced(True)

            return True
        else:
            return False

    def check_ship_placement(self, ship, x, y, rotation):
        "This function checks if a ship can be placed."
        #check if ship can be placed
        if rotation == ShipRotation.Horizontal:
            if x + ship.getLength() > 10:
                return False
            for i in range(ship.getLength()):
                if self.ship_board[y][x + i] != '.':
                    return False
        else:
            if y + ship.getLength() > 10:
                return False
            for i in range(ship.getLength()):
                if self.ship_board[y + i][x] != '.':
                    return False
        return True

    def make_move(self, x, y):
        "This function sets a hit on the board."
        #set hit

    def move_invalid(self, x, y):
        "This function returns that a move is invalid."
        #return move invalid
        if(x>len(self.board) or y>len(self.board) or x<0 or y<0):
            return True
        else:
            return False
    
    def move_already_made(self, x, y):
        "This function returns that a move has already been made."
        #return move already made
        if self.board[x][y] != '.':
            return True
        else:
            return False
        