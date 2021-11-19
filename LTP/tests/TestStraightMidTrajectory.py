import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SampleTrack import StraightTrackMap
from MidTrajectory import MidTrajectory
from Utils import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities

straight_track_map = StraightTrackMap(100, 10, 25, 5, 10)
straight_track_map.set_car_position(10, 10)

trajectory = MidTrajectory()
trajectory.compute_trajectory(straight_track_map)

final_trajectory = compute_velocities(trajectory.get_trajectory())

plot_track_map(straight_track_map, new_figure=True)
plot_trajectory(final_trajectory, new_figure=False)

end_plotting()