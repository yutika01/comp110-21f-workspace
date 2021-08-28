"""Using concantenation with relational operators."""
__author__: str = "730480382"

left: str = input("Left-hand side: ")
left_int: int = int(left)
right: str = input("Right-hand side: ")
right_int: int = int(right)
print(left + " < " + right + " is " + str((left_int < right_int)))
print(left + " >= " + right + " is " + str((left_int >= right_int)))
print(left + " == " + right + " is " + str((left_int == right_int)))
print(left + " != " + right + " is " + str((left_int != right_int)))