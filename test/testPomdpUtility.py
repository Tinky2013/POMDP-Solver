import unittest
from ddt import ddt, data, unpack

from src.pbvi import PBVI
from src.tigermodel import TigerModel
import sys
sys.path.append("..")

modelEnv = TigerModel()
pbvi = PBVI(modelEnv)

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
        testedTerm = pbvi.updateBelief(belief, action, observation)
        testingTerm = actualNormalizedBelief
        self.assertEqual(testedTerm, testingTerm)


if __name__ == '__main__':
    unittest.main()