#Random dice simulator

import random

min = 1
max = 6
i = 0
j = 0
k = []
def average(lst):
    return sum(lst)/len(lst)


roll = input("Would you like to roll dice? (Y/N)")

how_many = input("How many rolls would you like to do?")
count = int(how_many)

while roll == "Y" or roll == "y":
    print ("Rolling dies...")
    print ("The dice values are...")
    for i in range(count):
        j = (random.randint(min,max))
        k.append(j)
        i+=1
    print (k)
    print (average(k))
    roll = input("Would you like to go again?")
    how_many = input("How many rolls would you like to do?")
