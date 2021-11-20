"""
    handle ROS comunication
"""


from typing import List, Tuple
from Trajectory import Trajectory

def trajectory_to_ros(trajectory: Trajectory) -> Tuple[List[float], List[float], List[float], List[float]]:
    points_x = list(map(lambda x: x.position[0], trajectory.get_trajectory()))
    points_y = list(map(lambda x: x.position[1], trajectory.get_trajectory()))
    vel_x = list(map(lambda x: x.velocity_vector[0], trajectory.get_trajectory()))
    vel_y = list(map(lambda x: x.velocity_vector[0], trajectory.get_trajectory()))
    return points_x, points_y, vel_x, vel_y