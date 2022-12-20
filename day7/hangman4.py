#!/usr/bin/python3

#hangman game

import random

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
========
''', '''
  +---+                                                                                                                                                                   |   |                                                                                                                                                                   0   |                                                                                                                                                                  /|\  |                                                                                                                                                                  /    |
      |  
========
''', '''
  +---+ 
  |   |
  0   |
 /|\  |
      |                                                                                                                                                                       |                                                                                                                                                             
========
''', '''
   +---+
   |   |
   0   |
  /|   |                                                                                                                                                                       |                                                                                                                                                                       |                                                                                                                                                                 ========                                                                                                                                             
''', ''' 
  +---+
  |   |
  0   |
 /    |                                                                                                                                                                       |                                                                                                                                                                       |                                                                                                                                                                 ========                                                                                                                                                            
''', '''
  +---+ 
  |   |
  0   |
      |
      |                                     
      |  
========
''', '''
  +---+ 
  |   |
      |
      |
      |
      |
========
''']

end_of_game = False 
word_list = ["ardvark", "camel", "baboon"]   
chosen_word = random.choice(word_list).lower() 
lives = 6

#testing code

print(f'pssst, the solution is {chosen_word}')

display = []
for _ in  range(len(chosen_word)):  
    display += "_"     
print(display) 

while not end_of_game:     

    guess = input("Guess a letter: ")      

    for position in range(len(chosen_word)): 
        letter = chosen_word[position]          
        if letter == guess:  
            display[position] = letter
    
    if guess != chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")

    if "_" not in display:       
        end_of_game = True   
        print("You win")    
    
    print(stages[lives])
