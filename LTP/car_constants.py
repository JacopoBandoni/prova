"""
    Constants about the car
"""
MASS = 231.1 #kg

WIDTH = 1.45 # m
LENGTH = 2.5 # m

MIN_VELOCITY = 3  # [m/s] -> ~10 km/h
MAX_VELOCITY = 20 # [m/s] -> 72 km/h


FRICTION = 0.6 # God help us.

GRAVITY = 9.81 # [m/s^2]

F_GRIP = FRICTION * MASS * GRAVITY # [N] (0.6 * 231.1 * 9.81 = 1360,2546 [N])

MAX_THEORETICAL_FORWARD_FORCE = 2e3 # [N]

# We take the minimum between the theoretical maximum forward force
# and the maximum supported force by the grip of the tires.
MAX_ACCELERATION_FORCE = min(MAX_THEORETICAL_FORWARD_FORCE, F_GRIP) # [N]

MAX_ACCELERATION = MAX_ACCELERATION_FORCE / MASS # [m/s^2]


"""
tau = 1.  # factor between steer angle and front wheel angle

    mass = 231.1  # [kg]

    total_width = 1.45  # [m]

    total_length = 3.07  # [m]

    wheelbase = 1.53  # [m]

    track_front = 1.265  # [m] distance between front tyres

    track_rear = 1.135  # [m] distance between rear tyres

    _weight_balance = 0.42  # percent on rear axis

    yaw_inertia = 122.35  # [kg*m^2]

    cornering_stiffness_pacejka = 1029  # [N/rad] for each tyre

    cornering_stiffness_linear = 166 / 2  # [N/rad] computed from interpolating the Pacejka model value at slip_angle = 0.35




    mass_centre_height = .3  # [m] from the ground

    roll_centre_front = .25  # [m] vertical position of front roll centre

    roll_centre_rear = .45  # [m] vertical position of rear roll centre

    roll_stiffness_front = 357  # [Nm/deg] the resulting roll balance is ~0.51

    roll_stiffness_rear = 343  # [Nm/deg]




    brake_balance = .74  # (brake_front / brake_rear = ~2.87) percent of braking force on rear axis

    # r_r = .165  # [m] wheel radius

    rho = 1.1988  # air density

    S = 1.5  # [m^2] front area <------

    Cx = 1.13  # drag coefficient




    Cz = 1.86  # total aerodynamic lift (down-pushing)

    aerodynamic_balance = .56  # percent of total down-push force on rear axis

    mu = .75  # tyre adherence coefficient (same for each tyre) TODO: 1.1 seems to be closer to the real value




    max_lateral_velocity = 7.5  # [m/s]

    max_yaw_rate = cs.pi / 2  # [rad/s] -> 90 deg/s

    min_forward_velocity = 3.  # [m/s] -> ~10 km/h

    max_forward_velocity = 20.  # [m/s] -> 72 km/h

    max_steer_angle = cs.pi / 6.  # [rad] -> 30 deg

    max_acceleration = 2e3  # [N] 67 kW at full speed
"""
