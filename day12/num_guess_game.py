#!/usr/bin/python3
import random

EASY_TURNS = 10
HARD_TURNS = 5

def guess_check(guess, random_guess, turns):
    """checks guess against random_guess. Returns the number of turns remaining"""
    if guess > random_guess:
        print("Too High") 
        return turns - 1
    elif guess < random_guess:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {random_guess}")

def difficulty_level():
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_level == "easy":
        return EASY_TURNS
    elif game_level == "hard":
        return HARD_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_guess = random.randint(1, 100)
    print(f"{random_guess}")

    turns = difficulty_level()

    guess = 0
    while guess != random_guess:
        print(f"You have {turns} attempts to guess the number")
        guess = int(input("Make a guess: "))
        turns= guess_check(guess, random_guess, turns)
        if turns == 0:
            print("You 've run of guesses. You lose")
            return
        elif guess != random_guess:
            print("Guess again")

game()
