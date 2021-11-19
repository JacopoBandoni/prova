import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SampleTrack import CircleTrackMap
from MidTrajectory import MidTrajectory
from Utils import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities
from TrajectoryVisualizer import visualize_trajectory

import json

circle_track_map = CircleTrackMap(100, 10, 25, 5, 10)
circle_track_map.set_car_position(10, 10)

trajectory = MidTrajectory()
trajectory.compute_trajectory(circle_track_map)

final_trajectory = compute_velocities(trajectory.get_trajectory())

plot_track_map(circle_track_map, new_figure=True)
plot_trajectory(final_trajectory, new_figure=False)

end_plotting()

# d = {
#     'left_cones': {
#         'x': list(map(lambda x: x[0], circle_track_map.left_cones)),
#         'y': list(map(lambda x: x[1], circle_track_map.left_cones))
#     },
#     'right_cones': {
#         'x': list(map(lambda x: x[0], circle_track_map.right_cones)),
#         'y': list(map(lambda x: x[1], circle_track_map.right_cones))
#     },
#     'trajectory': {
#         'positions': {
#             'x': list(map(lambda x: x.position[0], trajectory)),
#             'y': list(map(lambda x: x.position[1], trajectory))
#         },
#         'velocities': list(map(lambda x: x.velocity, trajectory)),
#     }
# }

# with open('data.json', 'w') as f:
#     json.dump(d, f)