# queue.py
# Description: puts 10 random numbers in the queue
#               outputs all the values of the queue
#               takes numbers from the queue one at the time
#               prints it and thr numbers still in the queue


import random
queue = []
number_of_numbers = 10
rangeTo = 100

for n in range(0, number_of_numbers):
    queue.append(random.randint(0, rangeTo))

print("queue is {}".format(queue))

while len(queue) != 0:

    current_number = queue.pop(0)
    print (f"current number is {current_number} and the queue is {queue} ")
    # f was missing in this line so variables in curly brackets didn't get replaced by their value

print("the queue is now empty")
