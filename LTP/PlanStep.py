"""
    Represent a Step of our Car Planning
"""
from typing import Tuple


class PlanStep:
    """
        Define a Step of a Plan which consist to a tuple of position (x, y)
        and the desired car velocity
    """
    def __init__(self, position: Tuple[float, float], velocity: float):
        self.position = position
        self.velocity = velocity
