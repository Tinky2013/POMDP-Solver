import unittest
from ddt import ddt,data,unpack
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
        ('listen', 'tiger-left', 'tiger-left'),
    )
    @unpack
    def testTransition(self,state,action,nextState):
        tigerTransition = TigerTransition()
        testedTerm = tigerTransition(state,action,nextState)
        testingTerm = 1
        self.assertEqual(testedTerm,testingTerm)


@ddt
class TestReward(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('listen', 'tiger-left'),
    )
    @unpack
    def testReward(self,action,state):
        tigerReward = TigerReward()
        testedTerm = tigerReward(action,state)
        testingTerm = -1
        self.assertEqual(testedTerm, testingTerm)


@ddt
class TestObservation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('listen', 'tiger-left', 'tiger-left'),
    )
    @unpack
    def testObservation(self,action,state,observation):
        tigerObservation = TigerObservation()
        testedTerm = tigerObservation(action,state,observation)
        testingTerm = 0.85
        self.assertEqual(testedTerm, testingTerm)


if __name__ == '__main__':
    unittest.main()