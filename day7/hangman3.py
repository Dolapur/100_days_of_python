#!/usr/bin/python3

#hangman game 

import random  
word_list = ["ardvark", "camel", "baboon"]
chosen_word = random.choice(word_list).lower()            

#testing code
print(f'pssst, the solution is {chosen_word}') 

display = []   
for _ in  range(len(chosen_word)):
    display += "_" 
print(display)

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ") 

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess: 
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
