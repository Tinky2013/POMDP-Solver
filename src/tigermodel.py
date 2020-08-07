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
        self.discount = 0.75

        # tiger environment
        self.states = ['tiger-left', 'tiger-right']
        self.actions = ['listen', 'open-left', 'open-right']
        self.observations = ['tiger-left', 'tiger-right']

        # other settings
        self.initState = None
        self.currentState = self.initState or np.random.choice(self.states)

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
        rewards = TigerReward()
        return rewards(action, state)

    def observationFunction(self, action, state, observation):
        observations = TigerObservation()
        return observations(action, state, observation)

    def envFeedback(self, action):
        state = self.currentState   # after we have state and action, we can calculate observation, reward, nextState

        nextStateProbs = [self.transitionFunction(action, state, sj) for sj in self.states]
        nextState = self.states[chooseItemIdx(nextStateProbs)]

        observationProbs = [self.observationFunction(action, nextState, oj) for oj in self.observations]
        observation = self.observations[chooseItemIdx(observationProbs)]

        reward = self.rewardFunction(action, state)
        return nextState, observation, reward




