# nameAndAge2.py
#
# Author: Olga Knutova
#
# Description: Prompts user to right name and year of birth. 
#              Prints Hello "user's name" you are turning "user's age" this year
#
import datetime
currentDateTime = datetime.datetime.now ()
date = currentDateTime.date()
Cyear = int(date.strftime("%Y"))
name = input ("Enter your name: ")
Byear = int(input ("Enter the year you were born: "))
age = Cyear - Byear
print ('Hello ' + name + ', you are turning ' + str(age) + ' this year')

