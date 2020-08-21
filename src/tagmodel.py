'''
This part is for model setting

Import the transition function, reward funciton and observation of a tiger environment,
this file will initialize the model setting.
'''

from numpy import random
from tools.sampleUtility import chooseItemIdx
from Environment.tagEnvironment import TagTransition, TagReward, TagObservation
import numpy as np

class TagModel(object):
    def __init__(self):
        self.robotStates = ['[0,0]', '[0,1]', '[0,2]', '[0,3]', '[0,4]', '[0,5]', '[0,6]', '[0,7]', '[0,8]', '[0,9]',
                            '[1,0]', '[1,1]', '[1,2]', '[1,3]', '[1,4]', '[1,5]', '[1,6]', '[1,7]', '[1,8]', '[1,9]',
                            '[2,5]', '[2,6]', '[2,7]', '[3,5]', '[3,6]', '[3,7]', '[4,5]', '[4,6]', '[4,7]']
        self.opponentStates = ['[0,0]', '[0,1]', '[0,2]', '[0,3]', '[0,4]', '[0,5]', '[0,6]', '[0,7]', '[0,8]', '[0,9]',
                            '[1,0]', '[1,1]', '[1,2]', '[1,3]', '[1,4]', '[1,5]', '[1,6]', '[1,7]', '[1,8]', '[1,9]',
                            '[2,5]', '[2,6]', '[2,7]', '[3,5]', '[3,6]', '[3,7]', '[4,5]', '[4,6]', '[4,7]', '[tag]']
        # tag environment
        self.states = ['r' + i + 'n' + j for i in self.robotStates for j in self.opponentStates]
        self.actions = ['North','South','East','West','Tag']
        self.observations = ['r'+i for i in self.robotStates]+['sameblog']

        # other settings
        self.initState = None
        self.currentState = self.initState or np.random.choice(self.states)
        self.tagTransition = TagTransition()

    def __call__(self):
        pass

    def specifyEnvironmentArguments(self, param):
        self.discount = param['discount']

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
        transitions = TagTransition()
        return transitions(action, state, nextState)

    def rewardFunction(self, action, state):
        rewards = TagReward()
        return rewards(action, state)

    def observationFunction(self, action, state, observation):
        observations = TagObservation()
        return observations(action, state, observation)

    def generateInitBeliefPoints(self, numBelief):
        '''
        Here we used uniform random over the belief simplex
        '''
        self.robotStates = self.currentState[self.currentState.index('r') + 1:self.currentState.index('r') + 6]
        beliefPoints = [
            [random.uniform() if (
                s[s.index('r') + 1:s.index('r') + 6] == self.robotStates
            ) else 0.0 for s in self.states] for i in range(numBelief)
        ]
        return beliefPoints

    def generateUniformBeliefs(self):
        self.robotStates = self.currentState[self.currentState.index('r') + 1:self.currentState.index('r') + 6]
        Beliefs = [1 / len(self.observations) if (
                s[s.index('r') + 1:s.index('r') + 6] == self.robotStates
            ) else 0.0 for s in self.states]
        return Beliefs

    def getValidAction(self, state):
        robotState = state[state.index('r') + 1:state.index('r') + 6]
        validAction = [a for a in self.actions if self.tagTransition.judgeRobotActionValid(robotState, a)!=0]
        return validAction

    def envFeedback(self, state, action):
        # after we have state and action, we can calculate observation, reward, nextState
        print("Input state ", state, " and action ", action, " to the evironment.")
        nextStateProbs = [self.transitionFunction(action, state, sj) for sj in self.states]
        nextState = self.states[chooseItemIdx(nextStateProbs)]

        observationProbs = [self.observationFunction(action, nextState, oj) for oj in self.observations]
        observation = self.observations[chooseItemIdx(observationProbs)]
        reward = self.rewardFunction(action, state)

        return nextState, observation, reward

    def updateBelief(self, state, nextState, belief, action, observation):
        robotState = state[state.index('r') + 1:state.index('r') + 6]
        robotNextState = nextState[nextState.index('r') + 1:nextState.index('r') + 6]

        Idx = len(self.opponentStates) * self.opponentStates.index(robotState)
        nextIdx = len(self.opponentStates) * self.opponentStates.index(robotNextState)

        beliefpiece = belief[Idx:Idx + len(self.opponentStates)]
        cbelief = [0] * 870
        cbelief[nextIdx:nextIdx + len(self.opponentStates)] = beliefpiece

        newBelief = [
            self.observationFunction(action, sj, observation) * sum(
                [self.transitionFunction(action, si, sj) * float(cbelief[j]) for si in self.states]
            ) for j, sj in enumerate(self.states)
        ]

        # get the normalized belief
        normalizedFactor = sum(newBelief)
        assert (normalizedFactor != 0)
        normalizedBelief = [x / normalizedFactor for x in newBelief]
        return normalizedBelief  # return array with length=stateDim





