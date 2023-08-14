"""A dataclass is a class that helps you by defining all sorts of boilerplate methods such as: init, hash, order etc."""
from dataclasses import dataclass


@dataclass
class Person:
    """
    A person has:
        - A name
        - An age
        - Optional: A car

    A person should be able to buy a car and apply for insurance by requesting the cost
    """
    pass
