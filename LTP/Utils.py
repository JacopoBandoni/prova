from typing import List
from PlanStep import PlanStep
from TrackMap import TrackMap
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, griddata, interp2d
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb


def compute_spline(points: List[PlanStep]):
    xs = [plan_step.position[0] for plan_step in points]
    ys = [plan_step.position[1] for plan_step in points]
    
    xs, ys = zip(*list(set(zip(xs, ys))))

    tck,u=interpolate.splprep([xs,ys],s=0.0)

    x_i,y_i= interpolate.splev(np.linspace(0,1,len(points)),tck)
    dx_i,dy_i= interpolate.splev(np.linspace(0,1,len(points)),tck, der=1)
    ddx_i,ddy_i= interpolate.splev(np.linspace(0,1,len(points)),tck, der=2)

    return x_i,y_i,dx_i,dy_i,ddx_i,ddy_i


# Find line between two points
def find_line(p1, p2):
    if p1[0] == p2[0]:
        return (p1[0], None)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return (m, b)


def plot_track_map(track_map, new_figure=True):
    if new_figure:
        plt.figure()
    plt.title('Track Map')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter([x for x, _ in track_map.left_cones], [y for _, y in track_map.left_cones], color='blue', label='Left Cones')
    plt.scatter([x for x, _ in track_map.right_cones], [y for _, y in track_map.right_cones], color='yellow', label='Right Cones')
    if track_map.car_position is not None:
        plt.scatter(track_map.car_position[0], track_map.car_position[1], color='red', label='Car Position')
    plt.draw()

def plot_trajectory(trajectory, new_figure=False):
    if new_figure:
        plt.figure()
    plt.title('Trajectory')
    plt.xlabel('x')
    plt.ylabel('y')
    velocities = list(map(lambda x: x*3.6, [plan_step.velocity for plan_step in trajectory]))
    plt.scatter([plan_step.position[0] for plan_step in trajectory], [plan_step.position[1] for plan_step in trajectory], c=velocities, label='velocity (km/h)')
    plt.legend()
    plt.colorbar()
    plt.draw()

# Given a TrackMap and a trajectory plot them
def plot_track_map_and_trajectory(track_map: TrackMap, trajectory: List[PlanStep], new_figure=True):
    if new_figure:
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
    plt.legend()
    plt.draw()

def end_plotting():
    plt.show()