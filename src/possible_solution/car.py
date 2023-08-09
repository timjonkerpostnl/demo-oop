from dataclasses import dataclass, field

from src.possible_solution.brand import Brand
from src.possible_solution.climate_control import ClimateControl
from src.possible_solution.engine import Engine
from src.possible_solution.navigation import _get_direction


@dataclass
class Car:
    """
    A car has a number of features:
    - A brand name
    - An engine
    - A color
    - Convertible

    Things that a car should be able to do:
    Drive to a town:
        - Get direction
        - Start engine
        - Travel
        - Stop engine
    """
    brand: Brand
    engine: Engine
    color: str
    convertible: bool
    climate_control: ClimateControl = field(default=ClimateControl())

    def __post_init__(self):
        if not self.brand.is_engine_available(self.engine):
            raise ValueError(f"This {self.brand} cannot use {self.engine}")

    def _travel(self):
        print(f"Lovely travel in my {self.brand.brand_name}")
        self.climate_control.regulate_temperature(self.convertible)

    def drive_to(self, town: str):
        _get_direction(town)
        self.engine.start()
        self._travel()
        self.engine.stop()
