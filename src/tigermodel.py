'''
This part is for model setting

Import the transition function, reward funciton and observation of a tiger environment,
this file will initialize the model setting.
'''

from numpy import random
from tools.sampleUtility import chooseItemIdx
from Environment.tigerEnvironment import TigerTransition, TigerReward, TigerObservation
import numpy as np

class TigerModel(object):
    def __init__(self):
        # tiger environment
        self.states = ['tiger-left', 'tiger-right']
        self.actions = ['listen', 'open-left', 'open-right']
        self.observations = ['tiger-left', 'tiger-right']

        # other settings
        self.initState = None
        self.currentState = self.initState or np.random.choice(self.states)

    def __call__(self):
        pass


    def specifyEnvironmentArguments(self, param):
        self.discount = param['discount']
        self.rewardParam = param['reward_param']
        self.observationParam = param['observation_param']

    '''
    Here's some property of the tiger model
    '''
    @property
    def stateDim(self):
        return len(self.states)

    @property
    def actionDim(self):
        return len(self.actions)

    @property
    def observationDim(self):
        return len(self.observations)

    def transitionFunction(self, action, state, nextState):
        transitions = TigerTransition()
        return transitions(action, state, nextState)

    def rewardFunction(self, action, state):
        rewards = TigerReward(self.rewardParam)
        return rewards(action, state)

    def observationFunction(self, action, state, observation):
        observations = TigerObservation(self.observationParam)
        return observations(action, state, observation)

    def generateInitBeliefPoints(self, numBelief):
        '''
        Here we used uniform random over the belief simplex
        '''
        beliefPoints = [[random.uniform() for s in self.states] for i in range(numBelief)]
        return beliefPoints

    def generateUniformBeliefs(self):
        stateNUM = len(self.states)
        Beliefs = [1 / stateNUM for i in range(stateNUM)]
        return Beliefs





