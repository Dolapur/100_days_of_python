#!/usr/bin/python3

#program that prints the random person paying the bill

import random

print("Welcome, Who's paying the bill today")
names_string = input("Give me everybody's names, seperated by a comma\n")
names = names_string.split(", ")
len_names = len(names)
random_names = random.randint(0, (len_names - 1))
bill_payment = names[random_names]

print(f"{bill_payment} is going to buy the meal today!")
