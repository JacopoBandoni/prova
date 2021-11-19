import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Track_Generator import Track
from MidTrajectory import MidTrajectory
from Utils import plot_track_map, plot_trajectory, end_plotting
from ComputeVelocities import compute_velocities
from TrackMap import TrackMap
import json

custom_track = Track(10)
custom_track.load_track('track.json')

track_map = TrackMap(custom_track.get_left_cones(), custom_track.get_right_cones())

track_map.set_car_position(298, 235)
trajectory = MidTrajectory()
trajectory.compute_trajectory(track_map)

new_trajectory = compute_velocities(trajectory.get_trajectory())

plot_track_map(track_map, new_figure=True)
plot_trajectory(new_trajectory, new_figure=False)

# d = {
#     'left_cones': {
#         'x': list(map(lambda x: x[0], track_map.left_cones)),
#         'y': list(map(lambda x: x[1], track_map.left_cones))
#     },
#     'right_cones': {
#         'x': list(map(lambda x: x[0], track_map.right_cones)),
#         'y': list(map(lambda x: x[1], track_map.right_cones))
#     },
#     'trajectory': {
#         'positions': {
#             'x': list(map(lambda x: x.position[0], new_trajectory)),
#             'y': list(map(lambda x: x.position[1], new_trajectory))
#         },
#         'velocities': list(map(lambda x: x.velocity, new_trajectory)),
#     }
# }

# with open('data2.json', 'w') as f:
#     json.dump(d, f)

end_plotting()