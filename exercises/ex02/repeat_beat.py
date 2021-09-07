"""Repeating a beat in a loop."""

__author__ = "730480382"


# Begin your solution here...


beat: str = input("Insert beat: ")
num_repeat: int = int(input("Number of times to repeat: "))
output: str = ""
if (num_repeat <= 0):
    print("No beat...")
else: 
    output = beat
    while (num_repeat-1 > 0):
        output = output + " " + beat
        num_repeat = num_repeat - 1
    print (output)
