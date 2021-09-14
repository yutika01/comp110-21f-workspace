"""An exercise in remainders and boolean logic."""

__author__ = "730480382"

tarheel_int: int = int(input("Enter an int: "))
if (tarheel_int % 7 == 0):
    if (tarheel_int % 2 == 0):
        print("TAR HEELS")
    else: 
        print("HEELS")
elif (tarheel_int % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")