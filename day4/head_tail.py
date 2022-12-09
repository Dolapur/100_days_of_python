#!/usr/bin/python3

#virtual toss coin program

import random

random_num = random.randint(0, 1)

if random_num == 0:
    print("Tails")
else:
    print("Heads")

