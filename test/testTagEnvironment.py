import unittest
from ddt import ddt, data, unpack
from Environment.tagEnvironment import TagTransition

import sys
sys.path.append("..")


@ddt
class TestTagTransition(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('East', 'r[0,0]n[0,4]', 'r[0,1]n[0,5]', 0.8),
        ('West', 'r[0,9]n[0,5]', 'r[0,8]n[0,4]', 0.8),
    )
    @unpack
    def testTagTransition(self, action, state, nextState, actualProb):
        tagTransition = TagTransition()
        testedTerm = tagTransition(action, state, nextState)
        testingTerm = actualProb
        self.assertEqual(testedTerm, testingTerm)



if __name__ == '__main__':
    unittest.main()