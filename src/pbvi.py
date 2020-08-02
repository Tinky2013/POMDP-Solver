'''
This part is the core code of PBVI algorithm. It will include some utilities from other files

Notice (About My Code Design):
PBVI is a subclass of 'Solver'
all the algorithm will be included in the super class 'Solver'.
'''

import numpy as np
from tools.alphaVector import AlphaVector
from src.pomdputility import PomdpUtility

class PBVI(PomdpUtility):
    def __init__(self, modelEnv):
        PomdpUtility.__init__(self, modelEnv)
        self.beliefPoints = None
        self.alphaVectors = [AlphaVector(action=-1, value=np.zeros(modelEnv.stateDim))]
        self.solved = False

    def specifyAlgorithmArguments(self):
        pass

    def calculateReward(self):
        pass

    def calculateActionObservation(self, action, observation):
        gammaActionObservation = None
        return gammaActionObservation

    def createProjection(self):
        pass

    def computeCrossSum(self, gammaIntermediate):
        pass

    def findBestAction(self, gammaActionBelief):
        pass


    def solveHorizonT(self, T):
        if self.solved:
            return

        # every step the alpha-vector will be updated
        for step in range(T):
            # step 1: create projection
            gammaIntermediate = self.createProjection()
            # step 2: cross-sum operation
            gammaActionBelief = self.computeCrossSum(gammaIntermediate)
            # step 3: find best action for each belief point
            self.alphaVectors = self.findBestAction(gammaActionBelief)

        self.solved = True


    def getBestAction(self, belief):
        maxValue = -np.inf
        bestVectorIdx = None
        for alphaVector in self.alphaVectors:
            value = np.dot(alphaVector.value, belief)
            if value > maxValue:
                maxValue = value
                bestVectorIdx = alphaVector
        return bestVectorIdx.action


    def updateBelief(self, belief, action, observation):
        mEnv = self.modelEnv
        newBelief = []
        for sj in mEnv.states:
            Omega = mEnv.observationFunction(action, sj, observation)
            sumPart = 0
            for i, si in enumerate(mEnv.states):
                Trans = mEnv.transitionFunction(action, si, sj)
                sumPart += Trans * float(belief[i])
            newBelief.append(Omega * sumPart)
        # get the normalized belief
        normalizedFactor = sum(newBelief)
        normalizedBelief = [x / normalizedFactor for x in newBelief]
        return normalizedBelief  # return array with length=stateDim