import random


class ClimateControl:
    """
    Climate control:
        - If temperature > 20, turn on AC
        - If temperature < 20, turn on heater
        - If it is a convertible and temp > 25, open the roof and shut down the AC
    """

    def _get_outside_temperature(self) -> int:
        return random.randint(0, 40)

    def _heater_on(self) -> bool:
        return self._get_outside_temperature() < 20

    def _ac_on(self, has_convertible_roof: bool) -> bool:
        if has_convertible_roof and self._get_outside_temperature() > 25:
            return False
        return self._get_outside_temperature() > 20

    def regulate_temperature(self, has_convertible_roof: bool):
        self._heater_on()
        self._ac_on(has_convertible_roof)
