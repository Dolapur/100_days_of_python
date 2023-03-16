#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(former_text, shift_num):
    coded_text = ""

    for letter in former_text:
        position = alphabet.index(letter)
        new_position = position + shift_num
        new_letter = alphabet[new_position]
        coded_text += new_letter
    print(f"The encoded text is {coded_text}")

def decrypt(coded_text, shift_num):
    former_text = ""

    for letter in coded_text:
        position = alphabet.index(letter)
        new_position = position - shift_num
        text_letter = alphabet[new_position]
        former_text += text_letter
    print(f"The decoded text is {former_text}")

if direction == "encode":
    encrypt(former_text=text, shift_num=shift)
elif direction == "decode":
    decrypt(coded_text=text, shift_num=shift)
