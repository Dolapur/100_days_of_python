#!/usr/bin/python3

import random

from game_data import data

def format_data(account):
    """Format the account data into printable format"""  
    acc_name = account["name"] 
    acc_desc = account["description"]    
    acc_country = account["country"]
    return (f"{acc_name}, a {acc_desc}, from {acc_country}")  

def check_answer(guess, follower_a, follower_b):
    """Cgecking which account has more followers"""
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"
score = 0
continue_game = True
account_b = random.choice(data)
while continue_game:  
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}") 

    #Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    ##Get follower count of each account
    follower_a = account_a["follower_count"]
    follower_b = account_b["follower_count"]
    correct = check_answer(guess, follower_a, follower_b)

    if correct:
        score += 1
        print(f"You 're right! Current Score : {score}")
    else:
        continue_game = False
        print(f"Sorry that's wrong, final score: {score}")


