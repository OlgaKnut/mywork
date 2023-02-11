# lab3.1_random_fruit.py
# Description: prints out a random fruit

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A random fruit: {}". format(fruit))
