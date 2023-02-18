# lab4.1_grade.py

# Description: reads in a student's percentage mark 
# #and prints out the correcponding grade

percentage = float (input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print ("please enter a number between 0 and 100 ")
elif percentage >= 70:
    print ("Distinction")
elif percentage >= 60:
    print ("Merit 2")
elif percentage >= 50:
    print ("Merit 1")
elif percentage >= 40:
    print ("Pass")
else:
    print ("Fail")
