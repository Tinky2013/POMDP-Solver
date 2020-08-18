import unittest
from ddt import ddt, data, unpack
import numpy as np
from src.pbvi import PBVI
from src.tigermodel import TigerModel
import sys
from tools.alphaVector import AlphaVector
from array import array
from tools.sampleUtility import generateInitBeliefPoints

sys.path.append("..")

envParams = {
    'env_name': 'Tiger_env',
    'discount': 0.75,
    'reward_param': {
        'open_correct_reward': 10.,
        'open_incorrect_cost': -100.,
        'listen_cost': -1.,
    },
    'observation_param': {
        'obs_correct_prob': 0.85,
        'obs_incorrect_prob': 0.15,
    }
}

modelEnv = TigerModel()
modelEnv.specifyEnvironmentArguments(envParams)
algoParams = {
    'algo': 'pbvi',
    'horizon_T': 1,
    'expend_N': 1,
    'expend_method': 'RA',  # RA, SSRA, SSEA
    'num_belief': 100,
}
pbvi = PBVI(modelEnv)
beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['num_belief'])
pbvi.specifyAlgorithmArguments(beliefPoints, algoParams)

@ddt
class TestGetBestPlanningAction(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ([0.5,0.5],'listen'),
        ([0.6,0.4],'listen'),
        ([0.4,0.6],'listen'),
        ([0.99,0.01],'open-right'),
        ([0.01,0.99],'open-left'),
        ([1.,0.],'open-right'),
        ([0.,1.],'open-left'),
    )
    @unpack
    def testGetBestPlanningAction(self, belief, actualBestAction):

        testedTerm = pbvi.getPlanningAction(belief)
        testingTerm = actualBestAction
        self.assertEqual(testedTerm, testingTerm)

@ddt
class TestComputeGammaAStar(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ([-1.,-1.],'listen'),
        ([-100.,10.],'open-left'),
        ([10.,-100.],'open-right'),
    )
    @unpack
    def testComputeGammaAStar(self, reward, actionName):
        gammaAStar = pbvi.gammaAStar
        testedTerm = list(gammaAStar[actionName])
        testingTerm = reward
        self.assertEqual(testedTerm, testingTerm)

@ddt
class TestComputeGammaAOIntermediate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        (AlphaVector(action='listen', value=-1), 'listen', 'tiger-right'),
    )
    @unpack
    def testComputeGammaAOIntermediate(self, alpha, action, observation):
        pass


@ddt
class TestFindBestAlphaVector(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ({'listen': {0: np.array([-1., -1.]), 1: np.array([-1., -1.])},
          'open-left': {0: np.array([-100.,   10.]), 1: np.array([-100.,   10.])},
          'open-right': {0: np.array([10., -100.]), 1: np.array([10., -100.])}},
          0,[0.5,0.5],AlphaVector(action='listen', value=None)),
        ({'listen': {0: np.array([-1., -1.]), 1: np.array([-1., -1.])},
          'open-left': {0: np.array([-100., 10.]), 1: np.array([-100., 10.])},
          'open-right': {0: np.array([10., -100.]), 1: np.array([10., -100.])}},
         0, [0.91, 0.09], AlphaVector(action='open-right', value=None)),
        ({'listen': {0: np.array([-1., -1.]), 1: np.array([-1., -1.])},
          'open-left': {0: np.array([-100., 10.]), 1: np.array([-100., 10.])},
          'open-right': {0: np.array([10., -100.]), 1: np.array([10., -100.])}},
         0, [0.09, 0.91], AlphaVector(action='open-left', value=None)),
    )
    @unpack
    def testFindBestAlphaVector(self, gammaAB, bIdx, b, av):
        bestAlphaVec = pbvi.findBestAlphaVector(gammaAB, bIdx, b)
        testedTerm = bestAlphaVec.action
        testingTerm = av.action
        self.assertEqual(testedTerm, testingTerm)

