from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.possible_solution.person import Person


def insurance_cost(person: Person) -> int:
    """
    Insurance cost is based on a persons age and the brand they buy. The cost is 0 if the person has no car
    Cost = (100 - age) * 3 + brand_specific cost
    """
