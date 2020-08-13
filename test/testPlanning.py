import unittest
from ddt import ddt, data, unpack

from src.pbvi import PBVI
from src.tigermodel import TigerModel
import sys

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
pbvi = PBVI(modelEnv)
beliefPoints = generateInitBeliefPoints(modelEnv.states, stepsize=0.01)

@ddt
class TestPlanning(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ([0.5,0.5],'listen'),
        ([0.500001,0.499999],'listen'),
        ([0.499999,0.500001],'listen'),
        ([0.6, 0.4], 'listen'),
        ([0.4, 0.6], 'listen'),

        ([1,0],'open-right'),
        ([0,1],'open-left'),
        ([0.0000001,0.9999999],'open-left'),
        ([0.9999999,0.0000001],'open-right'),

        ([0.995, 0.005], 'open-right'),
        ([0.005, 0.995], 'open-left'),
    )
    @unpack
    def testGetBestPlanningAction(self, belief, actualBestAction):
        pbvi.specifyAlgorithmArguments(beliefPoints, 5)
        pbvi.getBestActionFromPlanning(T=2)
        testedTerm = pbvi.getBestAlphaVector(belief)
        testingTerm = actualBestAction
        self.assertEqual(testedTerm, testingTerm)

