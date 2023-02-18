# lab4.2topthree.py
# Description: generates random numbers
#                prints them out
#                prints out top 3

import random
how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

numbers = []

for i in range(0,how_many):
    numbers.append(random.randint(range_from,range_to))
print (f"{how_many} random number\t {numbers}")

top_ones = numbers.copy()
top_ones.sort(reverse = True)
print (f"The top {top_how_many} are \t\t{top_ones[0:top_how_many]}")
