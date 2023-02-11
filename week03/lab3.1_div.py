# lab3.1_div.py
# description: prompt user to enter two numbers
#              divides the first number by the second one
#              outputs the integer answer and reminder

x = int(input("Enter first number: "))
y = int(input("enter the number you want to divide by: "))
answer = int (x//y) # //gives the int division
remainder = x%y # % gives thr remainder
print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))
