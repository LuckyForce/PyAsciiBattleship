# File Info:
# Created: 2022-01-27
# Author: Adrian Schauer
# Description: This file contains the main function to initialize the game.

from game import Game
import display


def Main():
    display.welcome_message()
    input()
    print("Alright let's see if you are as good as my AI!")
    start()
    display.goodbye_message()


def start():
    display.game_selection()
    
    difficulty = input()
    while difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("Please enter either 1, 2 or 3.")
        difficulty = input()

    print("Alright if you think you have the guts, let's start the game!")
    print("-----INITIALIZING-----")

    game = Game(difficulty)

    print("-----FINISHED INITIALIZATION-----")
    print("-----STARTING SETUP-----")

    display.game_setup()

    game.setup()

    print("-----FINISHED SETUP-----")
    print("-----STARTING GAME-----")
    
    display.game_start()

    game.play()
    
    if(input("Do you wanna play the game again? (y/n)") == "y"):
        start()

if __name__ == '__main__':
    Main()
