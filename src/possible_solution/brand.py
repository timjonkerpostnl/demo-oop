from dataclasses import dataclass, field
from enum import Enum

from src.possible_solution.engine import Engine


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
    brand_name: BrandName = field(repr=True)
    max_hp: int = field(repr=True, init=False)
    insurance_cost: int = field(repr=True, init=False)

    def __post_init__(self):
        self.max_hp = self.determine_max_hp()
        self.insurance_cost = self.determine_insurance()

    def determine_max_hp(self) -> int:
        if self.brand_name == BrandName.suzuki:
            return 200
        elif self.brand_name == BrandName.mercedes:
            return 500
        elif self.brand_name == BrandName.mercedes:
            return 1000
        else:
            raise ValueError(f"Unknown brand type {self.brand_name}")

    def determine_insurance(self) -> int:
        if self.brand_name == BrandName.suzuki:
            return 100
        elif self.brand_name == BrandName.mercedes:
            return 1000
        elif self.brand_name == BrandName.mercedes:
            return 10000
        else:
            raise ValueError(f"Unknown brand type {self.brand_name}")

    def is_engine_available(self, engine: Engine) -> bool:
        return engine.horse_power <= self.max_hp
