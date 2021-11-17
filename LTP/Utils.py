from typing import List
from PlanStep import PlanStep
from TrackMap import TrackMap
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, griddata, interp2d
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def compute_spline(points: List[PlanStep]):
    xs = [plan_step.position[0] for plan_step in points]
    ys = [plan_step.position[1] for plan_step in points]
    tck,u=interpolate.splprep([xs,ys],s=0.0)

    x_i,y_i= interpolate.splev(np.linspace(0,0.5,200),tck)
    print(len(x_i))
    dx_i,dy_i= interpolate.splev(np.linspace(0,0.5,200),tck, der=1)

    plt.scatter(x_i, y_i, color='green', label='desired')
    plt.scatter(dx_i, dy_i, color='red', label='desired')

    plt.legend()
    plt.show()

# def compute_spline(points: List[PlanStep]):
#     x = [plan_step.position[0] for plan_step in points]
#     y = [plan_step.position[1] for plan_step in points]

#     f = interp2d(x, y, [1 for _ in points], kind='linear', copy=True, bounds_error=False, fill_value=None)
#     return f

#     x = [plan_step.position[0] for plan_step in points]
#     y = [plan_step.position[1] for plan_step in points]
#     f = interp1d(x, y, kind='cubic')
#     return f


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