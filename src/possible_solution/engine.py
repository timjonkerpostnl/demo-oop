from dataclasses import dataclass


@dataclass
class Engine:
    """
    An engine has a fixed horse power
    """
    horse_power: int

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine started")
