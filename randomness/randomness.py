"""
Randomness written by Joe Manlove

lecture on library imports and random fcts
revised 5/19/2020
revised 8/27/2026 to add this docstring
"""

# imports the random library
# import random
from random import randint, uniform, random

# assigns a random integer between 2 and 7 to x
# x = random.randint(2,7)
x = randint(2,7)

# print the result
print(x)

# get a random number using the uniform dist between 1 and 3 maybe including both ends
y = uniform(1,3)
# print the result
print(y)

# to get t between 5 and 8
# get a random number from 0 to 1 not including 1
t = random()
# (random between 0 and 3 not including 3) + 5
t = 3*t + 5
# print the result
print(t)

