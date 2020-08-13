import unittest
from ddt import ddt, data, unpack
from Environment.tigerEnvironment import TigerTransition, TigerReward, TigerObservation

import sys
sys.path.append("..")


@ddt
class TestTransition(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('listen', 'tiger-left', 'tiger-left', 1),
        ('listen', 'tiger-left', 'tiger-right', 0),
        ('open-left', 'tiger-left', 'tiger-left', 0.5),
        ('open-left', 'tiger-right', 'tiger-left',0.5),
    )
    @unpack
    def testTransition(self, state, action, nextState, actualProb):
        tigerTransition = TigerTransition()
        testedTerm = tigerTransition(state, action, nextState)
        testingTerm = actualProb
        self.assertEqual(testedTerm,testingTerm)


@ddt
class TestReward(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('listen', 'tiger-left', -1),
        ('open-left', 'tiger-left', -100),
        ('open-left', 'tiger-right', 10),
    )
    @unpack
    def testReward(self, action, state, actualReward):
        rewardParam = {
            'open_correct_reward': 10,
            'open_incorrect_cost': -100,
            'listen_cost': -1,
        }
        tigerReward = TigerReward(rewardParam)
        testedTerm = tigerReward(action, state)
        testingTerm = actualReward
        self.assertEqual(testedTerm, testingTerm)


@ddt
class TestObservation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('listen', 'tiger-left', 'tiger-left', 0.85),
        ('listen', 'tiger-right', 'tiger-left', 0.15),
        ('open-right', 'tiger-left', 'tiger-left',0.5),
    )
    @unpack
    def testObservation(self, action, state, observation, actualProb):
        observationParam = {
            'obs_correct_prob': 0.85,
            'obs_incorrect_prob': 0.15,
        }
        tigerObservation = TigerObservation(observationParam)
        testedTerm = tigerObservation(action, state, observation)
        testingTerm = actualProb
        self.assertEqual(testedTerm, testingTerm)


if __name__ == '__main__':
    unittest.main()