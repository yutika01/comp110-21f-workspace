"""Repeating a beat in a loop."""

__author__ = "730480382"


# Begin your solution here...

from _typeshed import HasFileno


beat: str = input("Insert beat: ")
num_repeat: int = int(input("Number of times to repeat: "))
if (num_repeat <= 0):
    print("No beat...")
else: 
    while (num_repeat > 0):
        print (beat)
        num_repeat = num_repeat - 1
