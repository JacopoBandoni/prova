import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from LTP.PlanStep import PlanStep
from Utils import compute_spline
from math import sqrt

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

def compute_velocities(trajectory: List[PlanStep], max_velocity=36) -> List[PlanStep]:
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
        new_trajectory[i].velocity = compute_velocity(curvature, 500, 243, max_velocity=36)
    print("R at each point:")
    # Compute avg curvature
    avg_curvature = sum(curvatures) / len(curvatures)
    print(avg_curvature)
    return new_trajectory
