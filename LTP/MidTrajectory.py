
"""
    Module MidTrajectory will compute the trajectory of the car
"""
from TrackMap import TrackMap
from PlanStep import PlanStep
from utility import euclidean_distance, find_closest_point, compute_middle_point

class Trajectory:
    """
        Represent an abstract Trajectory class used to represent
        the Trajectory desired for the car
    """
    def __init__(self, distance=euclidean_distance):
        self.distance = distance
        self.trajectory = []

    def compute_trajectory(self, track_map:TrackMap):
        """
            Compute the Trajectory desired by the car
        """

    def get_trajectory(self):
        """
            Get the computed trajectory for the car
        """
        return self.trajectory

class MidTrajectory(Trajectory):
    """
        Trajectory class which consist to remain in the middle between left and right cones
    """
    def __init__(self, distance=euclidean_distance):
        super().__init__(distance=distance)

    def compute_trajectory(self, track_map: TrackMap):
        cones_left = track_map.get_left_cones()
        cones_right = track_map.get_right_cones()

        for left_point in cones_left:
            right_point = cones_right[find_closest_point(left_point, cones_right, self.distance)]
            self.trajectory.append(PlanStep(compute_middle_point(left_point, right_point),
                                            velocity=0))
