
"""
    Module MidTrajectory will compute the trajectory of the car
"""
from typing import List
from TrackMap import TrackMap
from PlanStep import PlanStep
from Utils import euclidean_distance, find_closest_point, compute_middle_point

class Trajectory:
    """
        Represent an abstract Trajectory class used to represent
        the Trajectory desired for the car
    """
    def __init__(self, distance=euclidean_distance):
        self.distance = distance
        self.trajectory: List[PlanStep] = []

    def compute_trajectory(self, track_map:TrackMap):
        """
            Compute the Trajectory desired by the car
        """

    def get_trajectory(self):
        """
            Get the computed trajectory for the car
        """
        return self.trajectory

    def set_trajectory(self, new_trajectory: List[PlanStep]):
        """set new trajectory

        Args:
            List (PlanStep): new trajectory
        """
        self.trajectory = new_trajectory

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
            self.trajectory.append(PlanStep(compute_middle_point(left_point, right_point)))
    

if __name__ == '__main__':

    straight_track_map = CircleTrackMap(100, 10, 25, 5, 10)
    straight_track_map.set_car_position(10, 10)
    straight_track_map.show()
    partial_trajectory = MidTrajectory()

# class RandomTrajecory(Trajectory):
#     """
#         Trajectory class which consist to remain in the middle between left and right cones
#     """
#     def __init__(self, distance=euclidean_distance):
#         super().__init__(distance=distance)

#     def compute_trajectory(self, track_map: TrackMap):
#         cones_left = track_map.get_left_cones()
#         cones_right = track_map.get_right_cones()

#         for left_point in cones_left:
#             right_point = cones_right[find_closest_point(left_point, cones_right, self.distance)]
#             self.trajectory.append(PlanStep(compute_middle_point(left_point, right_point)))