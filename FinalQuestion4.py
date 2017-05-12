import random
import math

"""
This program creates a list of 30 random numbers, checks for duplicates, and prints the duplicates in a new list

newlist is the original list that's populated wiht random numbers.
dupelist is the second list populated with duplicates from with first list.
"""



newlist=[]
dupelist=[]


for i in range(30):
    newlist.append(random.randrange(0,100,1))

print("The original list follows:")
print(newlist)

for j in set(newlist):
    newlist.remove(j)

dupelist = list(set(newlist))

print("The following are duplicates in the previous list")
print(dupelist)