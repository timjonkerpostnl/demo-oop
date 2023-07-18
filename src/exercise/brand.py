from dataclasses import dataclass
from enum import Enum


class BrandName(Enum):
    suzuki = "Suzuki"  # Max hp: 200, Additional insurance cost: 100
    mercedes = "Mercedes"  # Max hp: 500, Additional insurance cost: 1000
    ferrari = "Ferrari"  # Max hp: 1000, Additional insurance cost: 10000


@dataclass
class Brand:
    """
    Brand should have the following attributes:
        - name
        - max_hp
        - insurance_cost
    Brand should be able to return:
        - If an engine is available
    """
