from typing import List, Tuple
import matplotlib.pyplot as plt

"""
Represents a track map defined by the left and right cones positions.
Each cone is represented by a tuple (x, y) which represent its position inside a Cartesian Plane.
"""
class TrackMap:
    def __init__(self, left_cones: List[Tuple[float, float]], right_cones: List[Tuple[float, float]]):
        self.left_cones = left_cones
        self.right_cones = right_cones
        self.car_position = None

    def set_car_position(self, x: float, y: float):
        self.car_position = (x, y)

    # TODO: our car is pointing to a direction
    def set_car_orientation(self, orientation: float):
        self.car_orientation = orientation
    
    def show(self):
        plt.figure()
        plt.title('Track Map')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.scatter([x for x, _ in self.left_cones], [y for _, y in self.left_cones], color='blue', label='Left Cones')
        plt.scatter([x for x, _ in self.right_cones], [y for _, y in self.right_cones], color='yellow', label='Right Cones')
        if self.car_position is not None:
            plt.scatter(self.car_position[0], self.car_position[1], color='red', label='Car Position')
        plt.show()