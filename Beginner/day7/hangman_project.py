#!/usr/bin/python3

import random

from hangman_word import word_list

chosen_word = random.choice(word_list).lower()

end_of_game = False
lives = 6  

from hangman_art import logo, stages
print(logo)


display = []                            
for _ in  range(len(chosen_word)):    
    display += "_"          
print(display)          

while not end_of_game:          
    guess = input("Guess a letter: ")        

    if guess in display:
        print(f"You 've already guessed {guess}")

    for position in range(len(chosen_word)):     
        letter = chosen_word[position]    
        if letter == guess:     
            display[position] = letter     

    if guess not in chosen_word: 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1                                                            
        if lives == 0:  
            end_of_game = True       
            print("You lose") 

    print(f"{' '.join(display)}")   

    if "_" not in display:    
        end_of_game = True   
        print(f'Yayyyyy, You win')    

    print(stages[lives])     

print(f'pssst, the solution is {chosen_word}')
