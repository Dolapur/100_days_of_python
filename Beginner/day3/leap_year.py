#!/usr/bin/python3

#program that print a leap year

year = int(input("which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")  
    else:
        print(f"The year {year} is  a leap year")
else:
    print(f"The year {year} is not a leap year")
