import unittest
from ddt import ddt,data,unpack
from src.tigermodel import TigerModel
modelEnv = TigerModel()

import sys
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

@ddt
class TestEnvFeedback(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('listen',-1),
    )
    @unpack
    def testFeedback(self, action, reward):
        modelEnv.specifyEnvironmentArguments(envParams)
        s, o, r = modelEnv.envFeedback(action)
        testedTerm = r
        testingTerm = reward
        self.assertEqual(testedTerm, testingTerm)

if __name__ == '__main__':
    unittest.main()