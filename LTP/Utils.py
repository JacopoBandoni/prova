from typing import List
from PlanStep import PlanStep
from TrackMap import TrackMap
import matplotlib.pyplot as plt
from scipy import interpolate
import matplotlib.pyplot as plt

def compute_distance(x1, x2):
    return ((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)**0.5

def compute_spline(points: List[PlanStep]):
    xs = [plan_step.position[0] for plan_step in points]
    ys = [plan_step.position[1] for plan_step in points]

    # TODO: Assert that there are no duplicated points.
    #       Note before we were just deleting them without removing them from the 'points': List[PlanStep]
    #       This caused a bug in the compute_velocities since we iterate over the points but'll have less
    #       derivative points => Causing an Out of bounds error
    print(len(list(zip(xs, ys))))
    print(len(list(set(zip(xs, ys)))))

    tck,u=interpolate.splprep([xs,ys],s=0.0)

    x_i,y_i= interpolate.splev(u,tck)
    dx_i,dy_i= interpolate.splev(u,tck, der=1)
    ddx_i,ddy_i= interpolate.splev(u,tck, der=2)

    return x_i,y_i,dx_i,dy_i,ddx_i,ddy_i


# Find line between two points
def find_line(p1, p2):
    if p1[0] == p2[0]:
        return (p1[0], None)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return (m, b)

def plot_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2])

def plot_track_map(track_map, new_figure=True):
    if new_figure:
        plt.figure()
    plt.title('Track Map')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter([x for x, _ in track_map.left_cones], [y for _, y in track_map.left_cones], color='blue', label='Left Cones')
    plt.scatter([x for x, _ in track_map.right_cones], [y for _, y in track_map.right_cones], color='yellow', label='Right Cones')
    # Plot starting point
    plt.scatter(track_map.left_cones[0][0], track_map.left_cones[0][1], color='black')
    plt.scatter(track_map.right_cones[0][0], track_map.right_cones[0][1], color='black')
    
    plot_line(track_map.left_cones[0][0], track_map.left_cones[0][1], track_map.left_cones[1][0], track_map.left_cones[1][1])
    plot_line(track_map.right_cones[0][0], track_map.right_cones[0][1], track_map.right_cones[1][0], track_map.right_cones[1][1])

    if track_map.car_position is not None:
        plt.scatter(track_map.car_position[0], track_map.car_position[1], color='red', label='Car Position')
    plt.draw()

def plot_trajectory(trajectory: List[PlanStep], new_figure=False):
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