"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, " 
    if isinstance(name, str):
        greeting += name
    else: 
        greeting += "COMP" + str(name)
    return greeting

# one argument
print(hello("Sally"))

# No arguments
print(hello())

# int arguments work too
print(hello(110))
