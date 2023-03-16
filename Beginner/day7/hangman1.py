#!/usr/bin/python3

#hangman game

import random

word_list = ["ardvark", "camel", "baboon"]
chosen_word = random.choice(word_list).lower()
guess = input("Guess a letter: ")

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
