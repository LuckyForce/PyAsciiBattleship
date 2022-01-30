#File Info:
#Created: 2020-01-29
#Author: Adrian Schauer
#Description: This file contains the interface for the ships.

import enum
from shiprotation import ShipRotation
from shiptype import ShipType

class Ship:
    def __init__(self, shiptype):
        "This function initializes the ship."

        self.shiptype = shiptype
        self.rotation = ShipRotation.Horizontal
        self.placed = False

        #Assigns the variables for the correct type.
        if(shiptype == ShipType.AircraftCarrier):
            self.name = "Aircraft Carrier"
            self.length = 5
            self.symbol = 'A'
        elif(shiptype == ShipType.Battleship):
            self.name = "Battleship"
            self.length = 4
            self.symbol = 'B'
        elif(shiptype == ShipType.Submarine):
            self.name = "Submarine"
            self.length = 3
            self.symbol = 'S'
        elif(shiptype == ShipType.Destroyer):
            self.name = "Destroyer"
            self.length = 3
            self.symbol = 'D'
        elif(shiptype == ShipType.PatrolBoat):
            self.name = "Patrol Boat"
            self.length = 2
            self.symbol = 'P'
    
    def __str__(self):
        "This function returns the name of the ship."
        return self.name

    def getLength(self):
        "This function returns the length of the ship."
        return self.length
    
    def getSymbol(self):
        "This function returns the symbol of the ship."
        return self.symbol
    
    def getRotation(self):
        "This function returns the rotation of the ship."
        return self.rotation
    
    def setRotation(self, rotation):
        "This function sets the rotation of the ship."
        self.rotation = rotation
    
    def isPlaced(self):
        "This function returns if the ship is placed."
        return self.placed
    
    def setPlaced(self, placed):
        "This function sets the placed variable."
        self.placed = placed