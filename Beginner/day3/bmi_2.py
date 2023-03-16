#!/usr/bin/python3

#Program that prints User's body mass index

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normalweight") 
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese") 

