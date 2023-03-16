#!/usr/bin/python3

#a program that calculate the sum and lenght of a set of inputed numbers with using the len() and sum() function

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height = total_height + height

student_height_len = 0
for length in student_heights:
    student_height_len += 1

average_height = total_height / student_height_len
print(round(average_height))
