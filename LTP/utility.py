"""
    Utility module used to define utility functions
"""

def convert_to_kmh(meters_second):
    """
        Convert m/s to km/h returning a floating value representing
        velocity in kilometers to hour

        Param:
            -meters_second(floating): meters second velocity
    """
    return meters_second * 3.6

def euclidean_distance(point_1, point_2):
    """
        Compute the euclidean distance between two points
    """
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**0.5

def find_closest_point(point, points, distance_function=euclidean_distance):
    """
        Find the closest point to a given point
    """
    min_distance = euclidean_distance(point, points[0])
    min_index = 0
    for index, candidate_point in enumerate(points):
        distance = distance_function(point, candidate_point)
        if distance < min_distance:
            min_distance = distance
            min_index = index
    return min_index

def compute_middle_point(left_point, right_point):
    """
        Find the middle point given two points
    """
    return (left_point[0] + right_point[0]) / 2, (left_point[1] + right_point[1]) / 2
