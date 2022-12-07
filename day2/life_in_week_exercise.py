#!/usr/bin/python3

#write a program that calculate days, weeks and year left if we are to live for 90 years

age = input("What is your current age?")
current_age = int(age)

years_left = 90 - current_age

days_left = years_left * 365 
week_left = years_left * 52
month_left = years_left * 12
print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left")
