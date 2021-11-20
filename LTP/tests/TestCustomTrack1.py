import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Trajectory import MidTrajectory
from GraphicUtility import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities
from TrackMap import TrackMap
from Utils import serialize_to_file, euclidean_distance_no_sqrt
from ROSInterface import trajectory_to_ros
import time

NAME_TEST = "TestCustomTrack1"

start_time = time.time()

custom_track = TrackMap()
custom_track.load_track('tests/tracks/TarascoRace.json')

custom_track.set_car_position((298, 235))
trajectory = MidTrajectory(distance=euclidean_distance_no_sqrt)
trajectory.compute_trajectory(custom_track)

trajectory.set_trajectory(compute_velocities(trajectory.get_trajectory()))

print("--- %s seconds ---" % (time.time() - start_time))

plot_track_map(custom_track, new_figure=True)
plot_trajectory(trajectory.get_trajectory(), new_figure=False)

serialize_to_file(custom_track.get_left_cones(), custom_track.get_right_cones(), trajectory.get_trajectory(), "./tests/output/" + NAME_TEST)

trajectory_to_ros(trajectory)

end_plotting()