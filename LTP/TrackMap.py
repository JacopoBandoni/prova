"""
    Module TrackMap manages Trackmap object and their representation
"""

from typing import List, Tuple
import matplotlib.pyplot as plt

class TrackMap:
    """
        Represent a Track Map defined by the left and right cones positions
        Each cone is represented by a tuple (x, y) which represent its position
        inside a Cartesian Plane.
    """
    def __init__(self, left_cones: List[Tuple[float, float]],
                 right_cones: List[Tuple[float, float]]):
        self.left_cones = list(set(left_cones))
        self.right_cones = list(set(right_cones))
        self.car_position = None
        self.car_orientation = 0.0

    def set_car_position(self, pos_x: float, pos_y: float):
        """
            Update Car Position
        """
        self.car_position = (pos_x, pos_y)

    def get_left_cones(self):
        """
            Obtain all Left cones inside the TrackMap
        """
        return self.left_cones

    def get_right_cones(self):
        """
            Obtain all Right Cones inside the TrackMap
        """
        return self.right_cones

    # TODO: our car is pointing to a direction
    def set_car_orientation(self, orientation: float):
        self.car_orientation = orientation

    def show(self):
        """
            Show Graphically the Track Map using Matplotlib
        """
        plt.figure()
        plt.title('Track Map')
        plt.xlabel('Position x')
        plt.ylabel('Position y')
        plt.scatter([pos_x for pos_x, _ in self.left_cones], [pos_y for _, pos_y in self.left_cones],
                    color='blue', label='Left Cones')
        plt.scatter([pos_x for pos_x, _ in self.right_cones], [pos_y for _, pos_y in self.right_cones],
                    color='yellow', label='Right Cones')
        if self.car_position is not None:
            plt.scatter(self.car_position[0], self.car_position[1], color='red', label='Car Pos')
        plt.show()
