#!/usr/bin/env python3
import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabets.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

game_on = True

while game_on:
    derived_list = [nato_dict[letter] for letter in input("Enter a word: ").upper() ]
    print(derived_list)
    if not input("Type 'y' to play again\n>> ") =='y':
        game_on = False
