"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730480382"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """Initialize the values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = values
    
    def __str__(self) -> str:
        """Convert a Simpy object to a str representation."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, num: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < num:
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values in terms of floats."""
        assert step != 0
        self.values = []
        i: float = start
        if start >= 0:
            while i < stop:
                self.values.append(i)
                i = i + step
        if start < 0:
            while i > stop:
                self.values.append(i)
                i = i + step
    
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        sum_value = sum(self.values)
        return sum_value
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload, add Simpy values together."""
        new: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            index: int = 0
            while index < len(rhs.values):
                new.values.append(rhs.values[index] + self.values[index])
                index += 1
        elif isinstance(rhs, float): 
            for each in self.values:
                new.values.append(each + rhs)
        return new

    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload, exponentiate Simpy values together."""
        new: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            index: int = 0
            while index < len(rhs.values):
                new.values.append(rhs.values[index] ** self.values[index])
                index += 1
        elif isinstance(rhs, float): 
            for each in self.values:
                new.values.append(each ** rhs)
        return new

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload, produce a mask based on the equality of a Simpy with another Simpy or float value."""
        output: list[bool] = []
        bool_value: bool = False
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            index: int = 0
            while index < len(rhs.values):
                if rhs.values[index] == self.values[index]:
                    bool_value = True
                output.append(bool_value)
                index += 1
        elif isinstance(rhs, float):
            for each in self.values:
                bool_value = False
                if each == rhs:
                    bool_value = True
                output.append(bool_value)
        return output

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Operator overload, produce a mask based on the greater than relationship of a Simpy with another Simpy or float value."""
        output: list[bool] = []
        bool_value: bool = False
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            index: int = 0
            while index < len(rhs.values):
                if rhs.values[index] > self.values[index]:
                    bool_value = True
                output.append(bool_value)
                index += 1
        elif isinstance(rhs, float):
            for each in self.values:
                bool_value = False
                if each > rhs:
                    bool_value = True
                output.append(bool_value)
        return output

    def __getitem__(self, rhs: int) -> float:
        """Operator overload, add the subscription operator with Simpy objects."""
        output: float = 0.0
        # More code
        return output