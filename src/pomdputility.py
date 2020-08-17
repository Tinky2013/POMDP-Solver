'''
This is the super class for all the algorithm designed to solve POMDP
'''

from abc import abstractmethod
from tools.sampleUtility import chooseItemIdx

class PomdpSolver(object):
    def __init__(self, modelEnv):
        self.modelEnv = modelEnv

    '''
    This part is the abstract method
    Notice: these abstract method should be implemented by certain algorithms
    '''
    @abstractmethod
    def getPlanningAction(self, belief):
        '''
        This is the POMDP solving part
        :param belief: your belief
        '''

    @abstractmethod
    def specifyAlgorithmArguments(self, *args):
        '''
        This function is used for adding specify arguments for specific solver
        :param args: additional arguments for the algorithm
        :return:
        '''

class EnvFeedback():
    def __init__(self, ModelEnv):
        self.modelEnv = ModelEnv

    def __call__(self, action):
        mEnv = self.modelEnv
        state = mEnv.currentState   # after we have state and action, we can calculate observation, reward, nextState

        nextStateProbs = [mEnv.transitionFunction(action, state, sj) for sj in mEnv.states]
        nextState = mEnv.states[chooseItemIdx(nextStateProbs)]

        observationProbs = [mEnv.observationFunction(action, nextState, oj) for oj in mEnv.observations]
        observation = mEnv.observations[chooseItemIdx(observationProbs)]

        reward = mEnv.rewardFunction(action, state)
        return nextState, observation, reward


class UpdateBelief():
    def __init__(self, ModelEnv):
        self.modelEnv = ModelEnv

    def __call__(self, belief, action, observation):
        mEnv = self.modelEnv
        newBelief = [
            mEnv.observationFunction(action, sj, observation)*sum(
                [mEnv.transitionFunction(action, si, sj) * float(belief[i]) for i, si in enumerate(mEnv.states)]
            ) for sj in mEnv.states
        ]
        # get the normalized belief
        normalizedFactor = sum(newBelief)
        normalizedBelief = [x / normalizedFactor for x in newBelief]
        return normalizedBelief  # return array with length=stateDim

