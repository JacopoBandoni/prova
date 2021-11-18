import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SampleTrack import StraightTrackMap
from MidTrajectory import compute_middle_trajectory
from Utils import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities

straight_track_map = StraightTrackMap(100, 10, 25, 5, 10)
straight_track_map.set_car_position(10, 10)

mid_trajectory = compute_middle_trajectory(straight_track_map)

trajectory = compute_velocities(mid_trajectory)

plot_track_map(straight_track_map, new_figure=True)
plot_trajectory(trajectory, new_figure=False)

end_plotting()