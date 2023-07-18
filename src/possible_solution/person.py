from dataclasses import dataclass, field
from typing import Optional

from src.possible_solution.brand import Brand
from src.possible_solution.car import Car
from src.possible_solution.engine import Engine
from src.possible_solution.isurance_company import insurance_cost


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

    def register_car(self, brand: Brand, engine: Engine, color: str, convertible: bool):
        self.car = Car(brand, engine, color, convertible)

    def apply_insurance(self) -> int:
        return insurance_cost(self)
