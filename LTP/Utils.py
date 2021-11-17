from typing import List
from PlanStep import PlanStep
from TrackMap import TrackMap
import matplotlib.pyplot as plt

# Find line between two points
def find_line(p1, p2):
    if p1[0] == p2[0]:
        return (p1[0], None)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return (m, b)


# Given a TrackMap and a trajectory plot them
def plot_track_map_and_trajectory(track_map: TrackMap, trajectory: List[PlanStep]):
    plt.figure()
    plt.title('Track Map')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter([x for x, _ in track_map.left_cones], [y for _, y in track_map.left_cones], color='blue', label='Left Cones')
    plt.scatter([x for x, _ in track_map.right_cones], [y for _, y in track_map.right_cones], color='yellow', label='Right Cones')
    if track_map.car_position is not None:
        plt.scatter(track_map.car_position[0], track_map.car_position[1], color='red', label='Car Position')
    # Plot trajectory
    plt.scatter([plan_step.position[0] for plan_step in trajectory], [plan_step.position[1] for plan_step in trajectory], color='green', label='Trajectory')
    plt.show()