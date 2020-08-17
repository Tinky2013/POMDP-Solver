import unittest
from ddt import ddt, data, unpack

from src.tigermodel import TigerModel
from src.pomdputility import EnvFeedback, UpdateBelief
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

modelEnv = TigerModel()
modelEnv.specifyEnvironmentArguments(envParams)
envFeedback = EnvFeedback(modelEnv)
updateBelief = UpdateBelief(modelEnv)

@ddt
class TestUpdateBelief(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ([0.5,0.5], 'open-left', 'tiger-left', [0.5,0.5]),
        ([0.5,0.5], 'open-right', 'tiger-left', [0.5,0.5]),
        ([0.5,0.5], 'open-left', 'tiger-right', [0.5,0.5]),
        ([0.5,0.5], 'open-right', 'tiger-right', [0.5,0.5]),
        ([0.5,0.5], 'listen', 'tiger-right', [0.15,0.85]),
        ([0.5,0.5], 'listen', 'tiger-left', [0.85,0.15]),
    )
    @unpack
    def testUpdateBelief(self, belief, action, observation, actualNormalizedBelief):
        testedTerm = updateBelief(belief, action, observation)
        testingTerm = actualNormalizedBelief
        self.assertEqual(testedTerm, testingTerm)

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
        s, o, r = envFeedback(action)
        testedTerm = r
        testingTerm = reward
        self.assertEqual(testedTerm, testingTerm)



if __name__ == '__main__':
    unittest.main()