#!/usr/bin/python3

#write a program that calculate the body mass index from a user's weight and height

height = input("Enter your height in m:")
weight = input("Enter your weight in kg:")
bmi_calculator = int(weight) / float(height) ** 2
bmi = int(bmi_calculator)
print(bmi)
