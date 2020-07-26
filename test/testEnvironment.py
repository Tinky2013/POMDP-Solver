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
        (None,None,None),
    )
    @unpack
    def testTransition(self,state,action,nextState):
        testedTerm = True
        testingTerm = True
        self.assertEqual(testedTerm,testingTerm)


@ddt
class TestReward(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        (None,None),
    )
    @unpack
    def testReward(self,action,state):
        testedTerm = True
        testingTerm = True
        self.assertEqual(testedTerm, testingTerm)


@ddt
class TestObservation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        (None,None,None),
    )
    @unpack
    def testObservation(self,action,state,observation):
        testedTerm = True
        testingTerm = True
        self.assertEqual(testedTerm, testingTerm)


if __name__ == '__main__':
    unittest.main()