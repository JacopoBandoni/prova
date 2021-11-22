from abc import ABC, abstractmethod
import random

class TrajectoryOptimizer:
    """
    a class handling the trajectory optimization from a middle circuit trajectory
    to a riskier one able to cut the circuit to achieve better performance
    """

    def __init__(self, trajectory):
        self.trajectory = trajectory 

    @abstractmethod
    def optimize(self, trackWidth):
        pass


# class RandomTrajectoryOptimizer(TrajectoryOptimizer):
#     """
#     ottimizza la traiettoria spostandola randomicamente e vedendo se migliora
#     """

#     def optimize(self, trackWidth, k):
#         """
#         trackWidth = larghezza della track (si suppone larghezza uguale in tutta la track)
#         k = numero di iterazioni
#         """

        

#         for i in range(0, k):
#             for point in self.trajectory:
#                 sample = random.randint(0, trackWidth)
#                 point = point - sample
            

#         return super().optimize()