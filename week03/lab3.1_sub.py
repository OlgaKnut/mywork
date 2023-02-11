# lab3.1_sub.py
# description: prompts user to input two numbers.
#              Subsracts second number from first
# imput reads in a string so we ned to convert it into an int to perform mathematical operations

x = int(input("Enter first number: "))
y = int(input ("Enter second number: "))
answer= x-y
print("{} minus {} is {} ".format(x, y, answer))
