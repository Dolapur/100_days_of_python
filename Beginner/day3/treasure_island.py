#!/usr/bin/python3

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

road = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if road == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait a boat. Type \"swim\" to swim across\n")
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if door == "yellow":
            print("\nYou win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
    
