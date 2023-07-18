import random
from typing import Tuple


def _get_direction(town: str) -> Tuple[float, float]:
    latitude = random.uniform(49, 53)
    longitude = random.uniform(3, 7)
    print(f"Direction of {town} is {latitude} and {longitude}")
    return latitude, longitude