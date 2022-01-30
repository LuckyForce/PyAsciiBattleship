#File Info: Created: 2020-01-30
#Author: Adrian Schauer
#Description: This file contains the enum for ship types.

import enum

class ShipType(enum.Enum):
    AircraftCarrier = "A"
    Battleship = "B"
    Submarine = "S"
    Destroyer = "D"
    PatrolBoat = "P"