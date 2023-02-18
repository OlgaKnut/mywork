# lab4.1is-even.py
# Description: asks the user to enter a number
#               tells if the number is even or odd
#               keeps prompting for a number until the user enters -1


number = int(input("enter an integer (-1 to quit): "))
while number != -1:

    if (number % 2) == 0:
        print (f"{number} is an even number")
        number = int(input("enter another integer (-1 to quit): "))
    else:
        print(f"{number} is an odd number")
        number = int(input("enter another integer (-1 to quit): "))
print("all done")

