'''
This is the super class for all the algorithm designed to solve POMDP
'''

from abc import abstractmethod


class PomdpUtility(object):
    def __init__(self, modelEnv):
        self.modelEnv = modelEnv

    '''
    This part is the abstract method
    Notice: these abstract method should be implemented by certain algorithms
    '''
    @abstractmethod
    def solveHorizonT(self, T):
        '''
        This is the POMDP solving part
        :param T: planing horizon
        '''

    @abstractmethod
    def updateBelief(self, belief, action, observation):
        '''
        This is the function update the belief distribution according to the environment feedback
        :param belief: previous belief distribution (array).
        :param action: action name (str).
        :param observation: observation name (str).
        :return: updated belief distribution (array).
        '''

    @abstractmethod
    def getBestAction(self, belief):
        '''
        This is the function help us choose the best action
        :param belief: belief distribution (array).
        :return: action name (str).
        '''

    @abstractmethod
    def specifyAlgorithmArguments(self, *args):
        '''
        This function is used for adding specify arguments for specific solver
        :param args: additional arguments for the algorithm
        :return:
        '''

    def envFeedback(self, action):
        '''
        Just for external usage
        :param action:
        :return: nextState, observation, reward
        '''
        return self.modelEnv.envFeedback(action)

