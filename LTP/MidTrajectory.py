
"""
- Data una traiettoria trovare velocità massima (metodo coi cerchi)
- Data una traiettoria trovare gli angoli che uniscono i vari punti (sterzo)
- Visualizzare traiettoria (magari con video?)
"""

from typing import List
from TrackMap import TrackMap
from PlanStep import PlanStep

# Given a cone find the closest cone in the 'list_of_cones'
def find_closest(cone, list_of_cones, start_it):
    def compute_distance(x1, x2):
        return pow(x2[0] - x1[0], 2) + pow(x2[1] - x1[1], 2)

    iterator_cones = start_it
    distance = compute_distance(cone, list_of_cones[iterator_cones])
    min_distance = distance
    iterations = 0
    
    while (iterations < len(list_of_cones)):
        distance = compute_distance(cone, list_of_cones[(iterator_cones+1) % len(list_of_cones)])
        if distance < min_distance:
            iterator_cones = (iterator_cones + 1) % len(list_of_cones)
            iterations+=1
        else:
            break
    
    return iterator_cones


# TODO: There is a bug, enjoy :D
def compute_middle_trajectory(track_map: TrackMap) -> List[PlanStep]:
    def compute_middle_point(x1, x2):
        return ((x1[0] + x2[0])/2, (x1[1] + x2[1])/2)
    cones_left = track_map.get_left_cones()
    cones_right = track_map.get_right_cones()
    trajectory = []
    iterator_right = 0 # Index of the closest cone to the right
    # Iterate through all the left cones
    for iterator_left in range(0, len(cones_left)):
        iterator_right = find_closest(cones_left[iterator_left], cones_right, iterator_right)

        point_x, point_y = compute_middle_point(cones_left[iterator_left], cones_right[iterator_right])
        trajectory.append(PlanStep((point_x, point_y), 0))
    
    #if points are too close, we should delete them
    return trajectory