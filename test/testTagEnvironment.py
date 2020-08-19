import unittest
from ddt import ddt, data, unpack
from Environment.tagEnvironment import TagTransition, TagReward, TagObservation

import sys
sys.path.append("..")

@ddt
class TestTagTransition(unittest.TestCase):
    def setUp(self):
        self.tagTransition = TagTransition()
        pass

    def tearDown(self):
        pass

    @data(
        # oppo stay
        # same row/col
        ('Tag', 'r[1,6]n[1,6]', 'r[1,6]ntagged', 1.0),  # oppo tagged
        ('Tag', 'r[1,0]n[1,9]', 'r[1,0]n[1,9]', 0.2),   # oppo at corner
        ('Tag', 'r[2,6]n[4,6]', 'r[2,6]n[4,6]', 0.2),   # oppo at edge
        ('Tag', 'r[0,8]n[1,8]', 'r[0,8]n[1,8]', 0.2),   # oppo at edge
        ('Tag', 'r[1,6]n[1,5]', 'r[1,6]n[1,5]', 0.2),   # oppo at mainland
        # diff row/col
        ('Tag', 'r[1,6]n[0,0]', 'r[1,6]n[0,0]', 1.0),   # oppo at corner
        ('Tag', 'r[0,0]n[1,8]', 'r[0,0]n[1,8]', 0.2),   # oppo at edge
        ('Tag', 'r[0,0]n[1,6]', 'r[0,0]n[1,6]', 0.2),   # oppo at mainland

        # oppo escape
        # oppoState at mainland (exp: [3,6])
        ('Tag', 'r[1,6]n[3,6]', 'r[1,6]n[3,5]', 0.8 / 3),
        ('Tag', 'r[3,7]n[3,6]', 'r[3,7]n[3,5]', 0.8 / 3),
        ('Tag', 'r[4,6]n[3,6]', 'r[4,6]n[3,5]', 0.8 / 3),
        ('Tag', 'r[2,7]n[3,6]', 'r[2,7]n[3,5]', 0.8 / 2),
        ('Tag', 'r[4,7]n[3,6]', 'r[4,7]n[3,5]', 0.8 / 2),
        # oppoState at north edge (exp: [1,2])
        ('Tag', 'r[0,2]n[1,2]', 'r[0,2]n[1,1]', 0.8 / 2),   # oppo [1,2]->[1,1]
        ('Tag', 'r[1,3]n[1,2]', 'r[1,3]n[1,1]', 0.8 / 2),
        ('Tag', 'r[2,5]n[1,2]', 'r[2,5]n[1,1]', 0.8 / 2),
        ('Tag', 'r[0,3]n[1,2]', 'r[0,3]n[1,1]', 0.8 / 1),
        ('Tag', 'r[1,1]n[1,2]', 'r[1,1]n[0,2]', 0.8 / 2),   # oppo [1,2]->[0,2]
        ('Tag', 'r[1,3]n[1,2]', 'r[1,3]n[0,2]', 0.8 / 2),
        ('Tag', 'r[2,5]n[1,2]', 'r[2,5]n[0,2]', 0.8 / 2),
        ('Tag', 'r[1,1]n[1,2]', 'r[1,1]n[1,3]', 0.8 / 2),   # oppo [1,2]->[1,3]
        ('Tag', 'r[0,2]n[1,2]', 'r[0,2]n[1,3]', 0.8 / 2),
        ('Tag', 'r[0,1]n[1,2]', 'r[0,1]n[1,3]', 0.8 / 1),
        ('Tag', 'r[4,5]n[1,8]', 'r[4,5]n[1,9]', 0.8 / 2),   # oppo [1,8]->[1,9]
        # oppoState at south edge (exp: [0,6])
        ('Tag', 'r[0,1]n[0,6]', 'r[0,1]n[0,7]', 0.8 / 2),   # oppo [1,6]->[1,7]
        ('Tag', 'r[1,6]n[0,6]', 'r[1,6]n[0,7]', 0.8 / 2),
        ('Tag', 'r[1,5]n[0,6]', 'r[1,5]n[0,7]', 0.8 / 1),
        ('Tag', 'r[1,6]n[0,6]', 'r[1,6]n[0,5]', 0.8 / 2),   # oppo [0,6]->[0,5]
        ('Tag', 'r[0,7]n[0,6]', 'r[0,7]n[0,5]', 0.8 / 2),
        ('Tag', 'r[1,7]n[0,6]', 'r[1,7]n[0,5]', 0.8 / 1),
        ('Tag', 'r[0,5]n[0,6]', 'r[0,5]n[1,6]', 0.8 / 2),   # oppo [0,6]->[1,6]
        ('Tag', 'r[0,7]n[0,6]', 'r[0,7]n[1,6]', 0.8 / 2),
        # oppoState at west edge (exp: [2,5])
        ('Tag', 'r[1,5]n[2,5]', 'r[1,5]n[3,5]', 0.8 / 2),   # oppo [2,5]->[3,5]
        ('Tag', 'r[2,6]n[2,5]', 'r[2,6]n[3,5]', 0.8 / 2),
        ('Tag', 'r[1,4]n[2,5]', 'r[1,4]n[3,5]', 0.8 / 2),
        ('Tag', 'r[1,6]n[2,5]', 'r[1,6]n[3,5]', 0.8 / 1),
        ('Tag', 'r[3,5]n[2,5]', 'r[3,5]n[1,5]', 0.8 / 2),   # oppo [2,5]->[1,5]
        ('Tag', 'r[2,6]n[2,5]', 'r[2,6]n[1,5]', 0.8 / 2),
        ('Tag', 'r[3,6]n[2,5]', 'r[3,6]n[1,5]', 0.8 / 1),
        ('Tag', 'r[3,5]n[2,5]', 'r[3,5]n[2,6]', 0.8 / 2),   # oppo [2,5]->[2,6]
        ('Tag', 'r[1,5]n[2,5]', 'r[1,5]n[2,6]', 0.8 / 2),
        ('Tag', 'r[1,4]n[2,5]', 'r[1,4]n[2,6]', 0.8 / 2),
        # oppoState at east edge (exp: [2,7])
        ('Tag', 'r[2,6]n[2,7]', 'r[2,6]n[3,7]', 0.8 / 2),  # oppo [2,7]->[3,7]
        ('Tag', 'r[1,7]n[2,7]', 'r[1,7]n[3,7]', 0.8 / 2),
        ('Tag', 'r[1,6]n[2,7]', 'r[1,6]n[3,7]', 0.8 / 1),
        ('Tag', 'r[3,7]n[2,7]', 'r[3,7]n[2,6]', 0.8 / 2),  # oppo [2,7]->[2,6]
        ('Tag', 'r[1,7]n[2,7]', 'r[1,7]n[2,6]', 0.8 / 2),
        ('Tag', 'r[1,8]n[2,7]', 'r[1,8]n[2,6]', 0.8 / 2),
        ('Tag', 'r[3,7]n[2,7]', 'r[3,7]n[1,7]', 0.8 / 2),  # oppo [2,7]->[1,7]
        ('Tag', 'r[2,6]n[2,7]', 'r[2,6]n[1,7]', 0.8 / 2),
        ('Tag', 'r[3,6]n[2,7]', 'r[3,6]n[1,7]', 0.8 / 1),
        # oppoState at corner
        # northwest
        ('Tag', 'r[0,0]n[1,0]', 'r[0,0]n[1,1]', 0.8 / 1),
        ('Tag', 'r[1,1]n[1,0]', 'r[1,1]n[0,0]', 0.8 / 1),
        ('Tag', 'r[2,5]n[1,0]', 'r[2,5]n[0,0]', 0.8 / 1),
        # northeast
        ('Tag', 'r[1,1]n[1,9]', 'r[1,1]n[0,9]', 0.8 / 1),
        ('Tag', 'r[2,5]n[1,9]', 'r[2,5]n[0,9]', 0.8 / 1),
        ('Tag', 'r[0,9]n[1,9]', 'r[0,9]n[1,8]', 0.8 / 1),
        # southeast
        ('Tag', 'r[0,1]n[0,9]', 'r[0,1]n[1,9]', 0.8 / 1),
        ('Tag', 'r[1,9]n[0,9]', 'r[1,9]n[0,8]', 0.8 / 1),
        # southwest
        ('Tag', 'r[1,0]n[0,0]', 'r[1,0]n[0,1]', 0.8 / 1),
        ('Tag', 'r[0,1]n[0,0]', 'r[0,1]n[1,0]', 0.8 / 1),

        # did not get caught
        ('East', 'r[1,5]n[1,6]', 'r[1,6]n[1,5]', 0.8 / 4),
        ('East', 'r[1,5]n[1,6]', 'r[1,6]n[1,7]', 0.8 / 4),
        ('East', 'r[1,5]n[1,6]', 'r[1,6]n[2,6]', 0.8 / 4),
        ('East', 'r[1,5]n[1,6]', 'r[1,6]n[0,6]', 0.8 / 4),
        ('East', 'r[1,5]n[1,6]', 'r[1,6]n[1,6]', 0.2),

        ('North', 'r[1,6]n[1,6]', 'r[2,6]n[0,6]', 0.8 / 3),
        ('North', 'r[1,6]n[1,6]', 'r[2,6]n[1,5]', 0.8 / 3),
        ('North', 'r[1,6]n[1,6]', 'r[2,6]n[1,7]', 0.8 / 3),

        ('South', 'r[1,1]n[0,1]', 'r[0,1]n[1,1]', 0.8 / 3),
        ('South', 'r[1,1]n[0,1]', 'r[0,1]n[1,1]', 0.8 / 3),
        ('South', 'r[1,1]n[0,1]', 'r[0,1]n[0,0]', 0.8 / 3),
        ('South', 'r[1,1]n[0,1]', 'r[0,1]n[0,1]', 0.2),

        ('West', 'r[1,1]n[1,0]', 'r[1,0]n[0,0]', 0.8 / 2),
        ('West', 'r[1,1]n[1,0]', 'r[1,0]n[1,1]', 0.8 / 2),
        ('West', 'r[1,1]n[1,0]', 'r[1,0]n[1,0]', 0.2),

        # other toy example
        ('East', 'r[1,4]n[3,6]', 'r[1,5]n[4,6]', 0.4),
        ('North', 'r[2,6]n[0,7]', 'r[3,6]n[0,8]', 0.8),
    )
    @unpack
    def testTagTransition(self, action, state, nextState, actualProb):
        testedTerm = self.tagTransition(action, state, nextState)
        testingTerm = actualProb
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[0,6]', '[1,6]', 'robot at south'),
        ('[2,6]', '[1,6]', 'robot at north'),
        ('[1,0]', '[1,6]', 'robot at west'),
        ('[1,9]', '[1,6]', 'robot at east'),
        ('[1,6]', '[1,6]', 'robot here'),

        ('[2,5]', '[1,6]', 'robot at northwest'),
        ('[2,7]', '[1,6]', 'robot at northeast'),
        ('[0,7]', '[1,6]', 'robot at southeast'),
        ('[0,5]', '[1,6]', 'robot at southwest'),
    )
    @unpack
    def testRobotIsAt(self, robotNextState, oppoState, actualRobotIsAt):
        testedTerm = self.tagTransition.theRobotIsAt(robotNextState, oppoState)
        testingTerm = actualRobotIsAt
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[1,6]','[1,5]', True),
        ('[1,6]','[1,6]', False),
    )
    @unpack
    def testJudgeOppoEscaping(self, oppoState, oppoNextState, actualIsEscaping):
        testedTerm = self.tagTransition.judgeOppoEscaping(oppoState, oppoNextState)
        testingTerm = actualIsEscaping
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[0,0]', 'North', 1),
        ('[0,0]', 'Tag', 1),
        ('[0,0]', 'East', 1),
        ('[0,0]', 'West', 0),
        ('[0,0]', 'South', 0),
        ('[1,5]', 'North', 1),
        ('[1,5]', 'Tag', 1),
        ('[1,5]', 'East', 1),
        ('[1,5]', 'West', 1),
        ('[1,5]', 'South', 1),
    )
    @unpack
    def testJudgeRobotActionValid(self, robotState, action, actualValidity):
        testedTerm = self.tagTransition.judgeRobotActionValid(robotState, action)
        testingTerm = actualValidity
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[1,4]', 'North', '[1,5]', 0),
        ('[1,4]', 'East', '[1,5]', 1),
        ('[1,4]', 'East', '[1,6]', 0),
        ('[1,4]', 'Tag', '[1,4]', 1),
    )
    @unpack
    def testJudgeRobotActionNextstateValid(self, robotState, action, robotNextState, actualValidity):
        testedTerm = self.tagTransition.judgeRobotActionNextstateValid(robotState, action, robotNextState)
        testingTerm = actualValidity
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[1,5]', '[1,5]', 1),
        ('[1,5]', '[1,6]', 1),
        ('[1,5]', '[1,4]', 1),
        ('[1,5]', '[2,5]', 1),
        ('[1,5]', '[0,5]', 1),
        ('[1,5]', '[1,3]', 0),
    )
    @unpack
    def testJudgeOppoPositionShiftValid(self, oppoState, oppoNextState, actualValidity):
        testedTerm = self.tagTransition.judgeOppoPositionShiftValid(oppoState, oppoNextState)
        testingTerm = actualValidity
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[2,6]', '[0,6]', '[0,7]', 1),
        ('[2,6]', '[0,6]', '[0,5]', 1),
        ('[2,6]', '[0,6]', '[1,5]', 0),
        ('[2,6]', '[0,5]', '[0,4]', 1),
        ('[2,6]', '[0,5]', '[1,5]', 0),
        ('[2,6]', '[0,5]', '[0,6]', 0),
    )
    @unpack
    def testJudgeOppoAvoidRobot(self, robotNextState, oppoState, oppoNextState, actualValidity):
        testedTerm = self.tagTransition.judgeOppoAvoidRobot(robotNextState, oppoState, oppoNextState)
        testingTerm = actualValidity
        self.assertEqual(testedTerm, testingTerm)


@ddt
class TestTagReward(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(
        ('Tag', 'r[1,6]n[1,6]', 10.0),
        ('Tag', 'r[1,6]n[1,5]', -10.0),
        ('North', 'r[1,6]n[1,6]', -1),
        ('North', 'r[1,6]n[1,5]', -1),
        ('South', 'r[1,6]n[1,6]', -1),
        ('South', 'r[1,6]n[1,5]', -1),
        ('East', 'r[1,6]n[1,6]', -1),
        ('East', 'r[1,6]n[1,5]', -1),
        ('West', 'r[1,6]n[1,6]', -1),
        ('West', 'r[1,6]n[1,5]', -1),
    )
    @unpack
    def testTagReward(self, action, state, actualReward):
        tagReward = TagReward()
        testedTerm = tagReward(action, state)
        testingTerm = actualReward
        self.assertEqual(testedTerm, testingTerm)


@ddt
class TestTagObservation(unittest.TestCase):
    def setUp(self):
        self.tagObservation = TagObservation()

    def tearDown(self):
        pass

    @data(
        ('North', 'r[1,6]n[4,7]', 'r[1,6]', 1),
        ('North', 'r[1,6]n[1,6]', 'sameblog', 1),
        ('Tag', 'r[1,6]n[1,6]', 'sameblog', 1),
        ('Tag', 'r[1,6]n[4,7]', 'r[1,6]', 1),
    )
    @unpack
    def testTagObservation(self, action, state, observation, actualObservationProb):
        tagObservation = TagObservation()
        testedTerm = tagObservation(action, state, observation)
        testingTerm = actualObservationProb
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('Tag', '[1,6]', 'tagged', 'sameblog', 1),
        ('North', '[1,6]', '[1,6]', 'sameblog', 1),
        ('North', '[1,6]', '[1,6]', 'r[1,6]', 0),
        ('North', '[1,6]', '[1,5]', 'sameblog', 0),
        ('North', '[1,6]', '[1,5]', 'r[1,6]', 1),
    )
    @unpack
    def testJudgeActionObservationValid(self, action, robotState, oppoState, observation, actualValidity):
        testedTerm = self.tagObservation.judgeActionObservationValid(action, robotState, oppoState, observation)
        testingTerm = actualValidity
        self.assertEqual(testedTerm, testingTerm)

    @data(
        ('[0,0]', 'North', 0),
        ('[0,0]', 'East', 0),
        ('[0,0]', 'South', 1),
        ('[0,0]', 'West', 1),
        ('[0,0]', 'Tag', 1),
    )
    @unpack
    def testJudgeRobotActionStateValid(self, robotState, action, actualValidity):
        testedTerm = self.tagObservation.judgeRobotActionStateValid(robotState, action)
        testingTerm = actualValidity
        self.assertEqual(testedTerm, testingTerm)


if __name__ == '__main__':
    unittest.main()