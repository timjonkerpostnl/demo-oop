from dataclasses import dataclass



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
