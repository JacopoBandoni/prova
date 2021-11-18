from typing import List, Tuple
import matplotlib.pyplot as plt
import math

class Track:

    def __init__(self, width: float):
        self.width: float = width                               # width of the track
        self.start: tuple[float, float] = (0, 0)                # starting position from which the track is generated (left part, not centered). 
                                                                #Updated when a new part is added (like the tail of a queue)
        self.direction: float = 0                               #current direction of the track
        self.left_cones: list[tuple[float, float]] = []         #list of left cones
        self.right_cones: list[tuple[float, float]] = []        #list of right cones

    def _straight_track_map(self, length: float, width: float, N_cones: int, start_x: float, start_y: float, direction: int = 0) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        """Generates a straight track of the given length and width.

        Args:
            length (float): the length of the track in meters
            width (float): the width of the track in meters
            N_cones (int): the number of cones to be placed on the track
            start_x (float): the x coordinate of the starting position of the track (left)
            start_y (float): the y coordinate of the starting position of the track (left)

        Returns:
            tuple[list[tuple[float, float]], list[tuple[float, float]]]: list of left and right cones
        """
        left_cones: list[tuple[float, float]] = []
        right_cones: list[tuple[float, float]] = []
        for i in range(0, length, length // N_cones):
            left_cones.append((start_x, start_y + i))
            right_cones.append((start_x + width, start_y + i))
        return (left_cones, right_cones)

    def _circle_track_map(self, radius: float, degree: int, width: float, N_cones: int, start_x: float, start_y: float, direction: int = 0) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        """Generates a curve track of the gicen radius, width and degree

        Args:
            radius (float): radius of the curve
            width (float): width of the track
            degree (int): degree of the curve
            N_cones (int): number of cones in the track
            start_x (float): the x coordinate of the starting position of the track (left)
            start_y (float): the y coordinate of the starting position of the track (left)

        Returns:
            tuple[list[tuple[float, float]], list[tuple[float, float]]]: [description]
        """
        left_cones: list[tuple[float, float]] = []
        right_cones: list[tuple[float, float]] = []
        print(start_x, start_y)
        for deg in range(0, degree, degree // N_cones):
            # Inner yellow cones
            x = start_x + radius * math.cos(math.radians(deg))
            y = start_y + radius * math.sin(math.radians(deg))
            left_cones.append((x-radius, y))
            # Outer blue cones
            x = start_x + (radius+width) * math.cos(math.radians(deg))
            y = start_y + (radius+width) * math.sin(math.radians(deg))
            right_cones.append((x-radius, y))
    
        return (left_cones, right_cones)

    def add_curve(self, radius: float, degrees: float, number_of_cones: int):
        """add a curve to the track

        Args:
            radius (float): radius of the curve. The smallest is the radius, the higher will be the curvature of the curve.
            degrees (float): how many degrees have the curve. For instance, if degree is 90, then the curve will be as follows:
                                                    *   *   *   *   *   *   *   *
                                                    *   *   *                   
                                                    *   *                       *
                                                    *                   *   *   *
                                                    *               *   *   *   *
            number_of_cones (int): number of cones the curve will have
        """
        new_left_cones, new_right_cones = self._circle_track_map(radius, degrees, self.width, number_of_cones, self.start[0], self.start[1])
        self.left_cones += new_left_cones
        self.right_cones += new_right_cones
        #setting the start position for the next track part. Note, add +1 to add offset for the next part
        self.start = (new_left_cones[-1][0], new_right_cones[-1][1])
        #setting the new direction in which we have to generate track. 
        self.direction = (self.direction + degrees)%360

    def add_straight(self, length: float, number_of_cones: int):
        """add a straight part to the track
        Args
            length (float): length of the straight par
            number_of_cones (int): number of cones the straight part ill have
        """
        new_left_cones, new_right_cones = self._straight_track_map(length, self.width, number_of_cones, self.start[0], self.start[1])
        self.left_cones += new_left_cones
        self.right_cones += new_right_cones
        #setting the start position for the next track part. Note, add +1 to add offset for the next part
        self.start = (new_left_cones[-1][0], new_right_cones[-1][1])

    def plot_track(self):
        """plot the current track
        """
        plt.figure()
        plt.title('Track Map')
        plt.xlabel('x')
        plt.ylabel('y')
        #unzip the cones for plotting
        left_x, left_y = zip(*self.left_cones)
        right_x, right_y = zip(*self.right_cones)
        #plot the cones
        plt.scatter(left_x, left_y, color='blue', label='Left Cones')
        plt.scatter(right_x, right_y, color='yellow', label='Right Cones')
        plt.show()

    def get_left_cones(self) -> List[Tuple[float, float]]:
        """returns left cones

        Returns:
            list[tuple[float, float]: list of left cones
        """
        return self.left_cones
    
    def get_right_cones(self) -> List[Tuple[float, float]]:
        """returns left cones

        Returns:
            list[tuple[float, float]: list of right cones
        """
        return self.right_cones

if __name__ == '__main__':
    track = Track(5)
    track.add_straight(20, 20)
    track.add_curve(50, 90, 10)
    track.plot_track()
