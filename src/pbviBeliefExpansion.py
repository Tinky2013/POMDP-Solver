import random
import numpy as np
from tools.sampleUtility import distanceL1

class BeliefExpension():
    '''
    In this class we have different belief-generation methods
    '''
    def __init__(self, mEnv):
        self.modelEnv = mEnv


    def randomBeliefSelection(self, oldBeliefPoints):
        '''
        RA (Random Belief Selection)
        '''
        mEnv = self.modelEnv
        newBeliefPoints = [[random.uniform(0,1) for s in mEnv.states]]
        return np.vstack((oldBeliefPoints, newBeliefPoints))

    def simulationWithRandomAction(self, oldBeliefPoints):
        '''
        SSRA (Stochastic Simulation with Random Action)
        '''
        mEnv = self.modelEnv
        belief = [random.uniform(0, 1) for s in mEnv.states]
        action = random.choice(mEnv.actions)
        nextState, observation, reward = mEnv.envFeedback(action)  # receive environment feedback
        newBelief = mEnv.updateBelief(belief, action, observation)  # update the belief
        newBeliefPoints = [newBelief]
        return np.vstack((oldBeliefPoints, newBeliefPoints))


    def simulationWithExploratoryAction(self, oldBeliefPoints):
        '''
        SSEA (Stochastic Simulation with Exploratory Action)
        '''
        mEnv = self.modelEnv
        belief = [random.uniform(0, 1) for s in mEnv.states]
        farthestBeliefPoints = None
        farthestDistance = -np.inf
        for action in mEnv.actions:
            nextState, observation, reward = mEnv.envFeedback(action)  # receive environment feedback
            newBelief = mEnv.updateBelief(belief, action, observation)  # update the belief
            totalDistance = 0
            for b in oldBeliefPoints:
                totalDistance += distanceL1(newBelief, list(b))

            if totalDistance > farthestDistance:
                farthestBeliefPoints = newBelief
                farthestDistance = totalDistance

        newBeliefPoints = [farthestBeliefPoints]
        return np.vstack((oldBeliefPoints, newBeliefPoints))


