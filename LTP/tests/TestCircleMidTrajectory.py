import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SampleTrack import CircleTrackMap
from MidTrajectory import compute_middle_trajectory
from Utils import plot_track_map_and_trajectory, compute_spline

straight_track_map = CircleTrackMap(100, 10, 25, 5, 10)
straight_track_map.set_car_position(10, 10)
mid_trajectory = compute_middle_trajectory(straight_track_map)

f = compute_spline(mid_trajectory)
# xs = [plan_step.position[0] for plan_step in mid_trajectory]
# ys = [plan_step.position[1] for plan_step in mid_trajectory]
# z = f(xs, ys)
# plt.scatter()

plot_track_map_and_trajectory(straight_track_map, mid_trajectory)