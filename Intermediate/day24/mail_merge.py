#!/usr/bin/env python3
#This program read the names from the input folder and send letters (using a template) to the output folder

PLACEHOLDER = "[name]"

with open("./Input/Names/names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/letter_template.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as invitation_letter:
            invitation_letter.write(new_letter)
