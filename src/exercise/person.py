from dataclasses import dataclass, field
from typing import Optional

from src.possible_solution.car import Car


@dataclass
class Person:
    name: str
    age: int
    car: Optional[Car] = field(default=None)
    """
    A person has:
        - A name
        - An age
        - Optional: A car

    A person should be able to register a car and apply for insurance by requesting the cost
    """
