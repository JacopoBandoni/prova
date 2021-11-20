"""
    Represent a Step of our Car Planning
"""
from typing import Tuple, List


class PlanStep:
    """
        Define a Step of a Plan which consist to a tuple of position (x, y)
        and the desired car velocity
    """
    def __init__(self, position: Tuple[float, float], velocity: float = 0, velocity_vector: List[Tuple[float, float]] = [0, 0]):
        self.position = position
        self.velocity = velocity
        self.velocity_vector = []