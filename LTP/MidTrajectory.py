
"""
- Data una traiettoria trovare velocità massima (metodo coi cerchi)
- Data una traiettoria trovare gli angoli che uniscono i vari punti (sterzo)
- Visualizzare traiettoria (magari con video?)
"""
from typing import List
from TrackMap import TrackMap
from PlanStep import PlanStep

def compute_distance(x1, x2):
    return ((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)**0.5

def find_closest_point(point, points):
    min_distance = compute_distance(point, points[0])
    min_index = 0
    for i in range(1, len(points)):
        distance = compute_distance(point, points[i])
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return min_index

def compute_middle_point(left_point, right_point):
    return (left_point[0] + right_point[0]) / 2, (left_point[1] + right_point[1]) / 2

def compute_middle_trajectory(track_map: TrackMap) -> List[PlanStep]:
    cones_left = track_map.get_left_cones()
    cones_right = track_map.get_right_cones()
    trajectory = []
    for left_point in cones_left:
        right_point = cones_right[find_closest_point(left_point, cones_right)]
        trajectory.append(PlanStep(compute_middle_point(left_point, right_point), velocity=0))
    return trajectory