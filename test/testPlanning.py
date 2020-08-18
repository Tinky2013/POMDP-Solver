import unittest
from ddt import ddt, data, unpack

from src.pbvi import PBVI
from src.tigermodel import TigerModel
import sys

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
    'expend_N': 5,
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

