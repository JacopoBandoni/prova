import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Track_Generator import Track
from MidTrajectory import compute_middle_trajectory
from Utils import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities
from TrackMap import TrackMap

custom_track = Track(10)
custom_track.load_track('track.json')

track_map = TrackMap(custom_track.get_left_cones(), custom_track.get_right_cones())

track_map.set_car_position(5, 0)
mid_trajectory = compute_middle_trajectory(track_map)

new_trajectory = compute_velocities(mid_trajectory)

plot_track_map(track_map, new_figure=True)
plot_trajectory(new_trajectory, new_figure=False)

end_plotting()