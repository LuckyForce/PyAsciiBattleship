# File Info:
# Created: 2020-01-27
# Author: Adrian Schauer
# Description: This file handles the output of the game.

def welcome_message():
    "This function gives out the welcome message."
    print("--------------------------------------")
    print("Welcome to the Battleship game!")
    print("This game is going to be against an AI enemy.")
    print("You have to guess the position of the enemy's ships.")
    print("And the enemy has to guess the position of your ships.")
    print("--------------------------------------")
    print("Do you think you can beat my AI?")
    print("If so press enter to start the game.")


def goodbye_message():
    "This function gives out the goodbye message."
    print("--------------------------------------")
    print("This game was made by Adrian Schauer.")
    print("Thanks for playing!")
    print("Goodbye!")
    print("--------------------------------------")


def game_selection():
    "This function gives out the selection message of the game."
    print("--------------------------------------")
    print("Arrghh! I am the enemy!")
    print("I am going to guess your ships!")
    print("You have to guess the position of my ships!")
    print("Good luck!")
    print("--------------------------------------")
    print("To make it easier to you I will let you decide how strong you want me to be")
    print("Please choose the difficulty of the game:")
    print("Enter either 1, 2 or 3. If you pick one, I am just going to guess. If you pick 2, I will destroy take the victory from you until you can't bear the humiliation anymore and if you pick 3, I am going to cheat, as pirates do arrrrrrghahahahaha!")


def game_setup():
    "This function gives out the setup message of the game."
    print("--------------------------------------")
    print("Hey! Stop right there you can't just beat my AI without nothing!")
    print("I am going to give you some ships!")
    print("Firstly I am going to give you a gigantic aircraft carrier with the length of 5 cells.")
    print("Secondly I am going to give you a battleship with the length of 4 cells.")
    print("Next I am going to give you a submarine with the length of 3 cells.")
    print("Moreover I am going to give you a destroyer with the length of 3 cells.")
    print("Then lastly I am going to give you a patrol boat with the length of 2 cells.")
    print("Now you just have to place your ships on the board.")
    print("If you want to play with more ships just add them to the list of ships. But remember you and the enemy will have the same amount of ships.")
    print("--------------------------------------")


def game_start():
    "This function gives out the start of the game."
    print("--------------------------------------")
    print("Alright let's start the game!")
    print("Let's see what you got!")
    print("Arrrghh!")
    print("--------------------------------------")


def game_state(game):
    "This function gives out the current state of the game."
    print("--------------------------------------")
    print("Difficulty:")
    print(game.diff)
    print("--------------------------------------")


def game_info():
    "This function gives out the information of how to play the game."


def player_move():
    "This function gives out the player move message."
    print("--------------------------------------")
    print("Your turn!")
    print("--------------------------------------")


def move_invalid():
    "This function gives out the invalid move message."
    print("--------------------------------------")
    print("Invalid move!")
    print("--------------------------------------")


def move_already_made():
    "This function gives out the already made move message."
    print("--------------------------------------")
    print("You already made a move here!")
    print("--------------------------------------")


def player_hit():
    "This function gives out the player hit message."
    print("--------------------------------------")
    print("You hit a ship!")
    print("--------------------------------------")


def player_miss():
    "This function gives out the player miss message."
    print("--------------------------------------")
    print("You missed!")
    print("--------------------------------------")


def enemy_hit():
    "This function gives out the enemy hit message."
    print("--------------------------------------")
    print("The enemy hit a ship!")
    print("--------------------------------------")


def enemy_miss():
    "This function gives out the enemy miss message."
    print("--------------------------------------")
    print("The enemy missed!")
    print("--------------------------------------")


def player_ship_selection():
    "This function gives out the player ship selection message."
    print("What ship do you want to place?")
    print("1. Destroyer, 2. Submarine, 3. Cruiser, 4. Battleship, 5. Carrier")
    print("Enter the number of the ship you want to place.")


def player_ship_placement():
    "This function gives out the player ship placement message."
    print("Where do you want to place the ship?")
    print("Enter the column and row of the field you want to place the ship.")
    print("Example: A1")
