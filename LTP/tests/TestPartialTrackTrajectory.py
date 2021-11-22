import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Trajectory import MidTrajectory
from GraphicUtility import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities
from TrackMap import TrackMap
from Utils import serialize_to_file, euclidean_distance_no_sqrt
from ROSInterface import trajectory_to_ros


# Defines a new partial track map with the first n_cones of the track map
def load_partial_track(complete_track: TrackMap, n_cones: int):
    return TrackMap(left_cones=complete_track.left_cones[:n_cones], right_cones=complete_track.right_cones[:n_cones])


NAME_TEST = "TestCustomTrack1"

custom_track = TrackMap()
custom_track.load_track('tests/tracks/TarascoRace.json')
custom_track.set_car_position((223, 300))

#trajectory = MidTrajectory(distance=euclidean_distance_no_sqrt)
#trajectory.compute_trajectory(custom_track)

partial_track = load_partial_track(custom_track, 10)
partial_track.set_car_position((223, 300))
trajectory = MidTrajectory(distance=euclidean_distance_no_sqrt)
trajectory.compute_trajectory(partial_track)
trajectory.set_trajectory(compute_velocities(trajectory.get_trajectory()))

plot_track_map(partial_track, new_figure=True)

plot_trajectory(trajectory.get_trajectory(), new_figure=False)

# serialize_to_file(custom_track.get_left_cones(), custom_track.get_right_cones(), trajectory.get_trajectory(), "./tests/output/" + NAME_TEST)

# trajectory_to_ros(trajectory)

end_plotting()