#!/usr/bin/python3


print("Welcome to the secret auction program.")

bids = {}
bidding_completed = False

def max_bidder(bidding_record):
    max_bid = 0
    winner = ""

    for bidder in (bidding_record):
        num_of_bid = bidding_record[bidder]
        if num_of_bid  > max_bid:          
            max_bid = num_of_bid   
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")

while not bidding_completed:  
    name = input("What is your name?: ")   
    price =int(input("What's your bid?:$ "))  
    bids[name] = price

    other_bid = input("Are there any other bidders? Type 'yes' or 'no'\n") 
    if other_bid == "no":
        bidding_completed = True
        max_bidder(bids)
