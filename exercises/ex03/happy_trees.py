"""Drawing forests in a loop."""

__author__ = "730480382"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
i: int = 0
depth: int = int(input("Depth: "))
while (depth >= 0):
    print(TREE)