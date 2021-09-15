"""Drawing forests in a loop."""

__author__ = "730480382"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
line: int = 1
num_print: int = 0
output: str = ""

while (line <= depth):
    num_print = line - 1
    while (num_print < line):
        output = output + " " + TREE
        num_print = num_print + 1
        print(output)
    line = line + 1
