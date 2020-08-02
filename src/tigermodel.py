'''
This part is for model setting

Import the transition function, reward funciton and observation of a tiger environment,
this file will initialize the model setting.
'''

import numpy as np

from Environment.tigerEnvironment import TigerTransition, TigerReward, TigerObservation

class TigerModel(object):
    def __init__(self):

        # tiger environment
        self.states = ['tiger-left', 'tiger-right']
        self.actions = ['listen', 'open-left', 'open-right']

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

    def transitionFunction(self, action, state, nextState):
        transitions = TigerTransition()
        return transitions(action, state, nextState)

    def rewardFunction(self, action, state):
        rewards = TigerReward()
        return rewards(action, state)

    def observationFunction(self, action, state, observation):
        observations = TigerObservation()
        return observations(action, state, observation)

    # TODO: Need Some Belief Points

    def generateUniformBeliefs(self):
        stateNUM = len(self.states)
        Beliefs = [1/stateNUM for i in range(stateNUM)]
        return Beliefs


