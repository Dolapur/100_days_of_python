#!/usr/bin/python3

#Project: Tip Calculator

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
bill_split = input("How many people to split the bill? ")

result_tip_percentage = (int(tip_percentage) / 100) * int(total_bill)

per_person_bill = (int(total_bill) + int(result_tip_percentage)) / int(bill_split)
person_bill = round(per_person_bill, 2)

print(f"Each person should pay: $ {person_bill}")
