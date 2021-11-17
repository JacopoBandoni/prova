"""
    Utility module used to define utility functions
"""
import numpy as np

def compute_velocity(curvature, grip_force, mass):
    """
        Compute Velocity of Curvature given Grip force, mass m and curvature R

        Param:
            -curvature(float): radius of Curvature
            -grip_force(float): grip force provided by the car
            -mass(float): mass of the Car

    """
    return np.sqrt((grip_force * curvature) / mass)

def convert_to_kmh(meters_second):
    """
        Convert m/s to km/h returning a floating value representing
        velocity in kilometers to hour 

        Param:
            -meters_second(floating): meters second velocity 
    """
    return meters_second * 3.6


