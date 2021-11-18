
"""
    Module MidTrajectory will compute the trajectory of the car
"""
from typing import List
from TrackMap import TrackMap
from PlanStep import PlanStep

def compute_distance(point_1, point_2):
    """
        Compute the euclidean distance between two points
    """
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**0.5

def find_closest_point(point, points):
    """
        Find the closest point to a given point
    """
    min_distance = compute_distance(point, points[0])
    min_index = 0
    for index, candidate_point in enumerate(points):
        distance = compute_distance(point, candidate_point)
        if distance < min_distance:
            min_distance = distance
            min_index = index
    return min_index

def compute_middle_point(left_point, right_point):
    """
        Find the middle point given two points
    """
    return (left_point[0] + right_point[0]) / 2, (left_point[1] + right_point[1]) / 2

def compute_middle_trajectory(track_map: TrackMap) -> List[PlanStep]:
    """
        Compute the Trajectory which consist to stay in the middle of the track
    """
    cones_left = track_map.get_left_cones()
    cones_right = track_map.get_right_cones()
    trajectory = []
    for left_point in cones_left:
        right_point = cones_right[find_closest_point(left_point, cones_right)]
        trajectory.append(PlanStep(compute_middle_point(left_point, right_point), velocity=0))
    return trajectory
