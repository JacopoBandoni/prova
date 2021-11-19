import os, sys

from Utils import compute_distance
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from PlanStep import PlanStep
from Utils import compute_spline, compute_distance
from math import sqrt
from CAR_CONSTANTS import MAX_VELOCITY, MAX_ACCELERATION, MAX_DECELERATION, F_GRIP, MIN_VELOCITY, MASS

# We need to reduce the final velocity
# 0.5 * a * t^2 + v_1 * t + (curr_pos - next_pos) = 0
# t = (-v_1 +- sqrt(v_1^2 - 2*a*(curr_pos - next_pos))) / a
# v_f = v_1 + a*t
def reduce_final_velocity(current_pos, next_pos, current_velocity, max_acceleration):
    new_time = (-2*current_velocity + sqrt((2*current_velocity)**2 + 8*max_acceleration * compute_distance(current_pos, next_pos))) / (2*max_acceleration)
    new_velocity = current_velocity + max_acceleration * new_time
    return new_velocity

def bound_velocities(trajectory: List[PlanStep], max_velocity, min_velocity, max_acceleration, max_deceleration) -> List[PlanStep]:
    new_trajectory = list(trajectory)
    # TODO: note the 2*len(trajectory) makes sense only in a closed loop (is this assumption correct?)
    for i in range(0, 2*len(trajectory)):
        # We check if from the current velocity and position we can reach the next velocity given the car constraints
        current_pos = new_trajectory[i % len(new_trajectory)].position
        next_pos = new_trajectory[(i+1) % len(new_trajectory)].position
        current_velocity = new_trajectory[i % len(new_trajectory)].velocity
        next_velocity = new_trajectory[(i+1) % len(new_trajectory)].velocity
        avg_velocity = (current_velocity + next_velocity) / 2
        time = compute_distance(current_pos, next_pos) / avg_velocity
        required_acc = (next_velocity - current_velocity) / time # v_f = v_i + a*t => a = v_f - v_i / t
        if required_acc > max_acceleration:
            # Given the max_acceleration of our car we cannot reach the final velocity
            # We then decrease the final velocity to the highest velocity we can reach
            new_velocity = reduce_final_velocity(current_pos, next_pos, current_velocity, max_acceleration)
            print(f"Reducing final velocity from {new_trajectory[(i+1) % len(trajectory)].velocity} to {new_velocity}")
            new_trajectory[(i+1) % len(trajectory)].velocity = new_velocity
        elif -max_deceleration < required_acc:
            # Given the max_deceleration of our car we cannot slow down to the final velocity
            # We then decrease the final velocity to the highest velocity we can reach starting from the final point
            # and assuming that our acceleration is the negative of the maximum deceleration
            new_velocity = reduce_final_velocity(next_pos, current_pos, next_velocity, -max_deceleration)
            print(f"Reducing initial velocity from {new_trajectory[i % len(trajectory)].velocity} to {new_velocity}")
            new_trajectory[i % len(trajectory)].velocity = new_velocity
    return new_trajectory

def compute_velocity(curvature: float, grip_force: float, mass: float, max_velocity: float = 36) -> float:
    """
        Compute Velocity of Curvature given Grip force, mass m and curvature R
        v_max = sqrt((R*grip_force)/mass)

        Param:
            -curvature(float): radius of Curvature
            -grip_force(float): grip force provided by the car
            -mass(float): mass of the Car
    """
    return min(sqrt((grip_force * curvature) / mass), max_velocity)

# TODO: Change function name to compute_radius or return just K and then use 1/K when you want the radius
def compute_curvature(f_x: float, f_y: float, df_x: float, df_y: float, ddf_x: float, ddf_y: float) -> float:
    """
    Compute the curvature of the trajectory
    :param f_x: f(x)
    :param f_y: f(y)
    :param df_x: first derivative of x
    :param df_y: first derivative of y
    :param ddf_x: second derivative of x
    :param ddf_y: second derivative of y
    :return: the curvature of the trajectory
    """
    num = abs(df_x * ddf_y - df_y * ddf_x)
    den = (df_x**2 + df_y**2)**(3/2)
    K = num / den
    return 1/K

# def compute_curvature(f_x: float, f_y: float, df_x: float, df_y: float, ddf_x: float, ddf_y: float) -> float:
#     """
#     Compute the curvature of the trajectory
#     :param f_x: f(x)
#     :param f_y: f(y)
#     :param df_x: first derivative of x
#     :param df_y: first derivative of y
#     :param ddf_x: second derivative of x
#     :param ddf_y: second derivative of y
#     :return: the curvature of the trajectory
#     """
#     return (df_x**2 + df_y**2)**3 / (df_x * ddf_y - df_y * ddf_x)**2

def compute_velocities(trajectory: List[PlanStep]) -> List[PlanStep]:
    """
    Compute the velocities of the trajectory.
    :param trajectory: the trajectory to compute the velocities
    :return: the trajectory with the velocities
    """
    # We need the first and second derivative of the trajectory to compute the Curvature needed
    # for the maximum velocity
    f_x, f_y, df_x, df_y, ddf_x, ddf_y = compute_spline(trajectory)
    curvatures = []
    new_trajectory = list(trajectory)
    for i in range(0, len(trajectory)):
        curvature = compute_curvature(f_x[i], f_y[i], df_x[i], df_y[i], ddf_x[i], ddf_y[i])
        curvatures.append(curvature)
        new_trajectory[i].velocity = compute_velocity(curvature, F_GRIP, MASS, MAX_VELOCITY)
    print("R at each point:")
    # Compute avg curvature
    avg_curvature = sum(curvatures) / len(curvatures)
    print(avg_curvature)
    return bound_velocities(new_trajectory, MAX_VELOCITY, MIN_VELOCITY, MAX_ACCELERATION, MAX_DECELERATION)
