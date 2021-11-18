import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SampleTrack import CircleTrackMap
from MidTrajectory import compute_middle_trajectory
from Utils import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities

circle_track_map = CircleTrackMap(100, 10, 25, 5, 10)
circle_track_map.set_car_position(10, 10)

mid_trajectory = compute_middle_trajectory(circle_track_map)

trajectory = compute_velocities(mid_trajectory)

plot_track_map(circle_track_map, new_figure=True)
plot_trajectory(trajectory, new_figure=False)

end_plotting()