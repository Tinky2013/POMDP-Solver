import unittest
from ddt import ddt,data,unpack
from src.tigermodel import TigerModel
modelEnv = TigerModel()

import sys
sys.path.append("..")

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
        s, o, r = modelEnv.envFeedback(action)
        testedTerm = r
        testingTerm = reward
        self.assertEqual(testedTerm, testingTerm)

if __name__ == '__main__':
    unittest.main()