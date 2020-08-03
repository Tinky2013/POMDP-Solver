'''
This part is the core code of PBVI algorithm. It will include some utilities from other files

Notice (About My Code Design):
PBVI is a subclass of 'PomdpUtility'
all the algorithm will be included in the super class 'PomdpUtilityr'.
'''

import numpy as np
from tools.alphaVector import AlphaVector
from src.pomdputility import PomdpUtility
from array import array

class PBVI(PomdpUtility):
    def __init__(self, modelEnv):
        PomdpUtility.__init__(self, modelEnv)
        self.modelEnv = modelEnv
        self.beliefPoints = None
        self.alphaVectors = [AlphaVector(action=-1, value=np.zeros(self.modelEnv.stateDim))]
        self.gammaReward = self.matrixReward()
        self.solved = False

    def specifyAlgorithmArguments(self, beliefPoints):
        PomdpUtility.specifyAlgorithmArguments(self)
        self.beliefPoints = beliefPoints

    def matrixReward(self):
        MatrixReward={
            a: np.frombuffer(array('d', [self.modelEnv.rewardFunction(a, s) for s in self.modelEnv.states]))
            for a in self.modelEnv.actions
        }
        return MatrixReward


    def calculateGammaIntermediate(self, action, observation):
        '''
        Calculation part for step 1
        The return should be: [v1, v2, ..., vi, ...]
        where vi=[alpha_i(state1), alpha_i(state2), ...]
        '''
        mEnv = self.modelEnv
        gammaSummation = []
        for alpha in self.alphaVectors:
            v = np.zeros(mEnv.stateDim)
            for i, si in enumerate(mEnv.states):
                for j, sj in enumerate(mEnv.states):
                    Trans = mEnv.transitionFunction(action, si, sj)
                    Omega = mEnv.observationFunction(action, sj, observation)
                    v[i] += Trans * Omega * alpha.value[j]
                v[i] *= mEnv.discount
            gammaSummation.append(v)
        return gammaSummation


    def createProjection(self):
        '''
        For every action-observation pair we need to compute a vector
        The return should be a dictionary: Gamma(a, o)
        '''
        mEnv = self.modelEnv
        gammaAO = {
            a: {
                o: self.calculateGammaIntermediate(a, o) for o in mEnv.observations
            } for a in mEnv.actions
        }
        return gammaAO


    def computeCrossSum(self, gammaAO):
        '''
        For every belief-action pair we need to compute a vector
        The return should be a dictionary: Gamma(b, a)
        '''
        mEnv = self.modelEnv
        gammaAB = {}
        for a in mEnv.actions:
            gammaAB[a] = {}
            for bIdx, b in enumerate(self.beliefPoints):
                gammaAB[a][bIdx] = self.gammaReward[a].copy()
                for o in mEnv.observations:     # find the best point for all possible observation
                    bestAlphaIdx = np.argmax(np.dot(gammaAO[a][o], b))
                    gammaAB[a][bIdx] += gammaAO[a][o][bestAlphaIdx]
        return gammaAB


    def findBestAction(self, gammaAB):
        mEnv = self.modelEnv
        newBestGammaVector, maxVal = [], -np.inf
        for bIdx, b in enumerate(self.beliefPoints):
            bestActionVal, bestAction = None, None
            for a in mEnv.actions:
                val = np.dot(gammaAB[a][bIdx], b)
                if bestActionVal is None or val>maxVal:
                    maxVal = val
                    bestActionVal = gammaAB[a][bIdx].copy()
                    bestAction = a
            newBestGammaVector.append(AlphaVector(action=bestAction, value=bestActionVal))
        return newBestGammaVector


    def solveHorizonT(self, T):
        if self.solved:
            return
        # every step the alpha-vector will be updated
        for step in range(T):
            # step 1: create projection
            gammaAO = self.createProjection()
            # step 2: cross-sum operation
            gammaAB = self.computeCrossSum(gammaAO)
            # step 3: find best action for each belief point
            self.alphaVectors = self.findBestAction(gammaAB)

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
