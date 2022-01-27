#File Info:
#Created: 2022-01-27
#Author: Adrian Schauer
#Description: This file contains the main function to initialize the game.

from game import Game
import display

def Main():
    display.welcome_message()
    display.game_selection()
    game = Game(2)
    game.play()
    print("Game ended")
    
if __name__ == '__main__':
    Main()