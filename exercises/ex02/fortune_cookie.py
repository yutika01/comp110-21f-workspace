"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730480382"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

print("Your fortune cookie says...")

rand_num = randint(1,4)
if (rand_num == 1):
    print("Something beautiful and unexpected is coming your way!")
else: 
    if (rand_num == 2):
        print("You are beautiful inside and out.")
    else: 
        if (rand_num == 3):
            print("Someone is thinking of you and missing you right now.")
        else:
            print("You are loved. ")

print("Now, go spread positive vibes!")