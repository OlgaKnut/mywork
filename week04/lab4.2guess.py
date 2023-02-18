# lab4.2guess.py
# Description: generates random number between 0 and 100
#               prompts user to guess a number
#               until the user gets it right

import random
number_to_guess = random.randint (0,100)

guess = int(input("Please guess the number between 0 and 100: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print ("too low")
    else: print("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", number_to_guess)
