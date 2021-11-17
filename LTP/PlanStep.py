
from typing import Tuple


class PlanStep:
    def __init__(self, position: Tuple[float, float], velocity: float):
        self.position = position
        self.velocity = velocity