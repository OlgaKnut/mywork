# lab3.1_random_generator.py
# Author: Olga Knutova
# description: prompts user to select the range
#              prints out a random number from selected range

import random

a = int(input("Enter number to start random selection from: "))
b = int(input("Enter number to stop random selection at: "))
number = random.randint (a,b)
print("here is a random number {}".format(number))
