
A TrackMap is defined by the left and right cones positions

Then, we call we compute a Trajectory, e.g.: by calling

        trajectory = MidTrajectory(track_map)
        
        trajectory = compute_velocities(trajectory, method='circles', max_velocity=130)