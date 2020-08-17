import random
import numpy as np
from tools.sampleUtility import distanceL1
from src.pomdputility import EnvFeedback, UpdateBelief

class BeliefExpension():
    '''
    In this class we have different belief-generation methods
    '''
    def __init__(self, mEnv):
        self.modelEnv = mEnv
        self.envFeedback = EnvFeedback(mEnv)
        self.updateBelief = UpdateBelief(mEnv)


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
        nextState, observation, reward = self.envFeedback(action)  # receive environment feedback
        newBeliefPoints = [self.updateBelief(belief, action, observation)]  # update the belief
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
            nextState, observation, reward = self.envFeedback(action)  # receive environment feedback
            newBelief = self.updateBelief(belief, action, observation)  # update the belief
            sumDistance = sum([distanceL1(newBelief, list(b)) for b in oldBeliefPoints])
            if sumDistance > farthestDistance:
                farthestBeliefPoints = newBelief
                farthestDistance = sumDistance
        return np.vstack((oldBeliefPoints, [farthestBeliefPoints]))



