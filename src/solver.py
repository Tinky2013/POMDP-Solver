'''
Solver is the super class for all the algorithm designed to solve POMDP
'''

from abc import abstractmethod

class Solver(object):
    def __init__(self, modelEnv):
        self.modelEnv = modelEnv

    '''
    This part is the specify functions
    '''
    def functionExp(self):
        return True

    '''
    This part is the abstract method
    Notice: these abstract method should be implemented by certain algorithms
    '''
    @abstractmethod
    def abstractMethodExp(self):
        '''
        your description
        :return:
        '''
