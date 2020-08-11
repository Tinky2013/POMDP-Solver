import random
import numpy as np

class BeliefExpension():
    def __init__(self, mEnv):
        self.modelEnv = mEnv

    def randomBeliefExpension(self, oldBeliefPoints):
        mEnv = self.modelEnv
        newBeliefPoints = [[random.uniform(0,1) for s in mEnv.states]]
        return np.vstack((oldBeliefPoints, newBeliefPoints))
