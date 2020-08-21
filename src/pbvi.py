'''
This part is the core code of PBVI algorithm. It will include some utilities from other files

Notice (About My Code Design):
PBVI is a subclass of 'PomdpUtility'
all the algorithm will be included in the super class 'PomdpUtilityr'.
'''

import numpy as np
from tools.alphaVector import AlphaVector
from .pbviBeliefExpansion import BeliefExpension
from array import array
import random

from Environment.tagEnvironment import TagTransition    # What?

np.random.seed()
random.seed()

class PBVI():
    def __init__(self, modelEnv):
        self.modelEnv = modelEnv
        self.beliefPoints = None
        self.alphaVectors = [AlphaVector(action=-1, value=np.zeros(self.modelEnv.stateDim))]
        self.gammaAStar = self.computeGammaAStar()
        self.solved = False

    def specifyAlgorithmArguments(self, beliefPoints, algoParam):
        self.beliefPoints = beliefPoints
        self.horizonT = algoParam['horizon_T']
        self.expendN = algoParam['expend_N']
        self.beliefExpension = BeliefExpension(self.modelEnv)

        if algoParam['expend_method'] == 'RA':
            self.beliefExpendMethod = self.beliefExpension.randomBeliefSelection
        elif algoParam['expend_method'] == 'SSRA':
            self.beliefExpendMethod = self.beliefExpension.simulationWithRandomAction
        elif algoParam['expend_method'] == 'SSEA':
            self.beliefExpendMethod = self.beliefExpension.simulationWithExploratoryAction


    def computeGammaAStar(self):
        gammaAStar={
            a: np.frombuffer(array('d', [self.modelEnv.rewardFunction(a, s) for s in self.modelEnv.states]))
            for a in self.modelEnv.actions
        }
        return gammaAStar


    def computeGammaAOIntermediate(self, alpha, action, observation):
        mEnv = self.modelEnv
        gammaAOvalList = [
            mEnv.discount * sum(
                [mEnv.transitionFunction(action, si, sj) * mEnv.observationFunction(action, sj, observation) * alpha.value[j]
                 for j, sj in enumerate(mEnv.states)]
            ) for i, si in enumerate(mEnv.states)
        ]
        return gammaAOvalList


    def computeGammaABIntermediate(self, a, b, gammaAO):
        mEnv = self.modelEnv
        obsValList = self.gammaAStar[a].copy()
        for o in mEnv.observations:  # find the best point for all possible observation
            bestAlphaIdx = np.argmax(np.dot(gammaAO[a][o], b))
            obsValList += gammaAO[a][o][bestAlphaIdx]
        return obsValList


    def findBestAlphaVector(self, gammaAB, bIdx, b):
        value = [np.dot(gammaAB[a][bIdx], b) for a in self.modelEnv.actions]
        bestActionIdx = random.choice(np.argwhere(value == np.max(value)))[0]
        bestAction = self.modelEnv.actions[bestActionIdx]
        bestActionVal = gammaAB[bestAction][bIdx].copy()
        return AlphaVector(action=bestAction, value=bestActionVal)


    def backUp(self):
        # step 1: create projection
        # For every action-observation pair we need to compute a vector
        gammaAO = {
            a: {
                o: [self.computeGammaAOIntermediate(alpha, a, o) for alpha in self.alphaVectors]
                for o in self.modelEnv.observations
            } for a in self.modelEnv.actions
        }

        # step 2: cross-sum operation
        # For every belief-action pair we need to compute a vector
        gammaAB = {
            a: {
                bIdx: self.computeGammaABIntermediate(a, b, gammaAO) for bIdx, b in enumerate(self.beliefPoints)
            } for a in self.modelEnv.actions
        }
        # step 3: update alpha-vectors (find best action for each belief point)
        self.alphaVectors = [self.findBestAlphaVector(gammaAB, bIdx, b) for bIdx, b in enumerate(self.beliefPoints)]

    def getBestActionVec(self, belief, state):
        value = [np.dot(alphaVector.value, belief) for alphaVector in self.alphaVectors]
        print("value:", value)
        validAlphaVectors = self.alphaVectors
        bestActionVecIdx = random.choice(np.argwhere(value == np.max(value)))[0]

        while validAlphaVectors[bestActionVecIdx].action not in self.modelEnv.getValidAction(state):
            validAlphaVectors[bestActionVecIdx].value = -np.inf
            bestActionVecIdx = random.choice(np.argwhere(value == np.max(value)))[0]

            val = [validAlphaVectors[i].value for i in range(len(validAlphaVectors))]
            if max(val)== -np.inf:
                print("No valid Action!")


        print("valid action:", self.modelEnv.getValidAction(state))
        for alphaVector in self.alphaVectors:
            print("AlphaAction: ", alphaVector.action)

        return self.alphaVectors[bestActionVecIdx]

    def getPlanningAction(self, state, belief):
        # Planning Process
        if self.solved == False:
            for expend in range(self.expendN):
                for iter in range(self.horizonT):
                    self.backUp()       # every step the alpha-vector will be updated
                #self.beliefPoints = self.beliefExpendMethod(self.beliefPoints)

            self.solved = True
            print("horizons have been solved!")
            print("-------------------------")

        # choose best action
        print("Now choose best action!")
        bestVector = self.getBestActionVec(belief, state)
        return bestVector.action





