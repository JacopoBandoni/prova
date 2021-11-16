from TrackMap import TrackMap
import math

# Generates a straight track of the given length and width.
#   length: the length of the track in meters
#   width: the width of the track in meters
#   N_cones: the number of cones to be placed on the track
#   start_x: the x coordinate of the starting position of the track
#   start_y: the y coordinate of the starting position of the track
def StraightTrackMap(length: float, width: float, N_cones: int, start_x: float, start_y: float) -> TrackMap:
    left_cones: list[tuple[float, float]] = []
    right_cones: list[tuple[float, float]] = []
    for i in range(0, length, length // N_cones):
        left_cones.append((start_x, start_y + i))
        right_cones.append((start_x + width, start_y + i))
    return TrackMap(left_cones, right_cones)


def CircleTrackMap(radius: float, width: float, N_cones: int, start_x: float, start_y: float) -> TrackMap:
    left_cones: list[tuple[float, float]] = []
    right_cones: list[tuple[float, float]] = []
    
    for grado in range(0, 360, 360 // N_cones):
        # Inner yellow cones
        x = start_x + radius * math.cos(math.radians(grado))
        y = start_y + radius * math.sin(math.radians(grado))
        right_cones.append((x, y))
        # Outer blue cones
        x = start_x + (radius+width) * math.cos(math.radians(grado))
        y = start_y + (radius+width) * math.sin(math.radians(grado))
        left_cones.append((x, y))
    
    return TrackMap(left_cones, right_cones)


if __name__ == '__main__':
    straight_track_map = StraightTrackMap(100, 10, 25, 5, 10)
    straight_track_map.set_car_position(10, 10)
    straight_track_map.show()

    straight_track_map = CircleTrackMap(100, 10, 25, 5, 10)
    straight_track_map.set_car_position(10, 10)
    straight_track_map.show()