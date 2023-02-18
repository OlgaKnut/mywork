# lab4.2average.py
# Description: reads in numbers until the user enters 0
#               prints numbers back out
#                prints average

numbers = []
number = int(input("enter number (0to quit): "))

while number !=0:
    numbers.append (number)
    number = int(input("enter another (0 to quit): "))
for value in numbers:
    print (value)
average = float(sum(numbers)) / len(numbers)
print (f"The average is {average}")
