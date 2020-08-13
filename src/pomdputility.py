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
    def getBestActionFromPlanning(self, belief):
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

