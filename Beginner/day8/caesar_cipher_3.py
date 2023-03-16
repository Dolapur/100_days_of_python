#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_num, coded_direction):
    end_text = ""
    
    for letter in start_text:
        position = alphabet.index(letter)
        if coded_direction == "decode":     
            new_position = position - shift_num
        elif coded_direction == "encode":
            new_position = position + shift_num
        end_text += alphabet[new_position] 
    print(f"The {coded_direction}d text is {end_text}")

caesar(start_text=text, shift_num=shift, coded_direction=direction) 


