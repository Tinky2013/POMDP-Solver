
class TagTransition():
    def __init__(self):
        self.robotValidMoving = {
            ('North', -1, 0): 1.0,
            ('South', 1, 0): 1.0,
            ('East', 0, 1): 1.0,
            ('West', 0, -1): 1.0,
            ('Tag', 0, 0): 1.0,
        }
        self.oppoValidMoving = {
            (-1, 0): 1.0,
            (1, 0): 1.0,
            (0, 1): 1.0,
            (0, -1): 1.0,
            (0,0): 1.0,
        }
        self.oppoEscapeDirection = {
            ('0', 0, 0): 1.0,
            ('N', 1, 0): 1.0,
            ('S', -1, 0): 1.0,
            ('E', 0, 1): 1.0,
            ('W', 0, -1): 1.0,
            ('EN', 0, 1): 1.0, ('EN', 1, 0): 1.0,
            ('ES', 0, 1): 1.0, ('ES', -1, 0): 1.0,
            ('WS', 0, -1): 1.0, ('WS', -1, 0): 1.0,
            ('WN', 0, -1): 1.0, ('WN', 1, 0): 1.0,
        }
        self.oppoMovingProb = {
            ('N','[1,1]'): 1.0, ('N','[1,2]'): 1.0, ('N','[1,3]'): 1.0, ('N','[1,4]'): 1.0, ('N','[1,8]'): 1.0, ('N','[4,6]'): 1.0, ('N','[1,0]'): 1.0, ('N','[1,9]'): 1.0, ('N','[4,5]'): 1.0, ('N','[4,7]'): 1.0,
            ('N','[2,5]'): 0.8, ('N','[3,5]'): 0.8, ('N','[2,7]'): 0.8, ('N','[3,7]'): 0.8, ('N','[1,5]'): 0.8, ('N','[1,6]'): 0.8, ('N','[1,7]'): 0.8, ('N','[2,6]'): 0.8, ('N','[3,6]'): 0.8,

            ('S','[0,1]'): 1.0, ('S','[0,2]'): 1.0, ('S','[0,3]'): 1.0, ('S','[0,4]'): 1.0, ('S','[0,5]'): 1.0, ('S','[0,6]'): 1.0, ('S','[0,7]'): 1.0, ('S','[0,8]'): 1.0, ('S','[0,0]'): 1.0, ('S','[0,9]'): 1.0,
            ('S','[2,5]'): 0.8, ('S','[3,5]'): 0.8, ('S','[2,7]'): 0.8, ('S','[3,7]'): 0.8, ('S','[1,5]'): 0.8, ('S','[1,6]'): 0.8, ('S','[1,7]'): 0.8, ('S','[2,6]'): 0.8, ('S','[3,6]'): 0.8,

            ('E','[4,7]'): 1.0, ('E','[1,9]'): 1.0, ('E','[0,9]'): 1.0, ('E','[2,7]'): 1.0, ('E','[3,7]'): 1.0,
            ('E','[4,6]'): 0.8, ('E','[1,8]'): 0.8, ('E','[1,1]'): 0.8, ('E','[1,2]'): 0.8, ('E','[1,3]'): 0.8, ('E','[1,4]'): 0.8, ('E','[0,1]'): 0.8, ('E','[0,2]'): 0.8, ('E','[0,3]'): 0.8, ('E','[0,4]'): 0.8, ('E','[0,5]'): 0.8, ('E','[0,6]'): 0.8, ('E','[0,7]'): 0.8, ('E','[0,8]'): 0.8, ('E','[1,5]'): 0.8, ('E','[1,6]'): 0.8, ('E','[1,7]'): 0.8, ('E','[2,6]'): 0.8, ('E','[3,6]'): 0.8,

            ('W','[4,5]'): 1.0, ('W','[1,0]'): 1.0, ('W','[0,0]'): 1.0, ('W','[2,5]'): 1.0, ('W','[3,5]'): 1.0,
            ('W','[4,6]'): 0.8, ('W','[1,8]'): 0.8, ('W','[1,1]'): 0.8, ('W','[1,2]'): 0.8, ('W','[1,3]'): 0.8, ('W','[1,4]'): 0.8, ('W','[0,1]'): 0.8, ('W','[0,2]'): 0.8, ('W','[0,3]'): 0.8, ('W','[0,4]'): 0.8, ('W','[0,5]'): 0.8, ('W','[0,6]'): 0.8, ('W','[0,7]'): 0.8, ('W','[0,8]'): 0.8, ('W','[1,5]'): 0.8, ('W','[1,6]'): 0.8, ('W','[1,7]'): 0.8, ('W','[2,6]'): 0.8, ('W','[3,6]'): 0.8,

            ('EN','[4,7]'): 1.0, ('EN','[1,9]'): 1.0,
            ('EN','[4,5]'): 0.8, ('EN','[4,6]'): 0.8, ('EN','[1,8]'): 0.8, ('EN','[2,7]'): 0.8, ('EN','[3,7]'): 0.8, ('EN','[1,1]'): 0.8, ('EN','[1,2]'): 0.8, ('EN','[1,3]'): 0.8, ('EN','[1,4]'): 0.8,
            ('EN','[2,5]'): 0.4, ('EN','[3,5]'): 0.4, ('EN','[1,5]'): 0.4, ('EN','[1,6]'): 0.4, ('EN','[1,7]'): 0.4, ('EN','[2,6]'): 0.4, ('EN','[3,6]'): 0.4,

            ('WN','[4,5]'): 1.0, ('WN','[1,0]'): 1.0,
            ('WN','[4,7]'): 0.8, ('WN','[4,6]'): 0.8, ('WN','[1,8]'): 0.8, ('WN','[2,5]'): 0.8, ('WN', '[3,5]'): 0.8, ('WN','[1,1]'): 0.8, ('WN','[1,2]'): 0.8, ('WN','[1,3]'): 0.8, ('WN','[1,4]'): 0.8,
            ('WN','[2,7]'): 0.4, ('WN','[3,7]'): 0.4, ('WN','[1,5]'): 0.4, ('WN','[1,6]'): 0.4, ('WN', '[1,7]'): 0.4, ('WN','[2,6]'): 0.4, ('WN','[3,6]'): 0.4,

            ('ES','[0,9]'): 1.0,
            ('ES','[1,9]'): 0.8, ('ES','[2,7]'): 0.8, ('ES','[3,7]'): 0.8, ('ES','[0,1]'): 0.8, ('ES','[0,2]'): 0.8, ('ES','[0,3]'): 0.8,  ('ES','[0,4]'): 0.8, ('ES','[0,5]'): 0.8, ('ES','[0,6]'): 0.8, ('ES','[0,7]'): 0.8, ('ES','[0,8]'): 0.8,
            ('ES','[1,8]'): 0.4, ('ES','[1,5]'): 0.4, ('ES','[1,6]'): 0.4, ('ES','[1,7]'): 0.4, ('ES','[2,6]'): 0.4, ('ES','[3,6]'): 0.4,

            ('WS','[0,0]'): 1.0,
            ('WS','[1,0]'): 0.8, ('WS','[2,5]'): 0.8, ('WS','[3,5]'): 0.8, ('WS','[0,1]'): 0.8, ('WS','[0,2]'): 0.8, ('WS','[0,3]'): 0.8, ('WS','[0,4]'): 0.8, ('WS','[0,5]'): 0.8, ('WS','[0,6]'): 0.8, ('WS','[0,7]'): 0.8, ('WS','[0,8]'): 0.8,
            ('WS','[1,1]'): 0.4, ('WS','[1,2]'): 0.4, ('WS','[1,3]'): 0.4, ('WS','[1,4]'): 0.4, ('WS','[1,5]'): 0.4, ('WS','[1,6]'): 0.4, ('WS','[1,7]'): 0.4, ('WS','[2,6]'): 0.4, ('WS','[3,6]'): 0.4,

            ('0','tagged'): 1.0,
        }

    def __call__(self, action, state, nextState):
        robotState = state[state.index('r')+1:state.index('r')+6]
        oppoState = state[state.index('n')+1:state.index('n')+6]
        robotNextState = nextState[nextState.index('r')+1:nextState.index('r')+6]
        if nextState[nextState.index('n')+1:]=='tagged':
            oppoNextState = 'tagged'
        else:
            oppoNextState = nextState[nextState.index('n')+1:nextState.index('n')+6]

        # which direction is the robot moving towards
        robotDirection = list(map(lambda v:v[1]-v[0], zip(eval(robotState), eval(robotNextState))))
        isRobotNextStateValid = self.robotValidMoving.get((action, robotDirection[0], robotDirection[1]), 0.0)
        # which direction is the opponent moving towards
        oppoDirection = list(map(lambda v:v[1]-v[0], zip(eval(oppoState), eval(oppoNextState))))
        isOpponentNextStateValid = self.oppoValidMoving.get((oppoDirection[0], oppoDirection[1]), 0.0)
        # relative direction (fixed opponent, robot is in which direction)
        relativeDirection = list(map(lambda v: v[1] - v[0], zip(eval(robotNextState), eval(oppoState))))
        relativeDirectionIdx = self.judgePosition(relativeDirection[0], relativeDirection[1]) # which way should oppo escape
        isOppoAvoidRobot = self.oppoEscapeDirection.get((relativeDirectionIdx, oppoDirection[0], oppoDirection[1]), 0.0)

        oppoNextStateProb = self.oppoMovingProb.get((relativeDirectionIdx, oppoState), 0.0)
        nextStateProb = isRobotNextStateValid*isOpponentNextStateValid*isOppoAvoidRobot*oppoNextStateProb
        return nextStateProb

    def judgePosition(self, x, y):
        if x==0:
            if y==0:
                return '0'
            elif y>0:
                return 'E'
            else:
                return 'W'

        elif x>0:
            if y==0:
                return 'N'
            elif y>0:
                return 'EN'
            else:
                return 'WN'

        else:
            if y==0:
                return 'S'
            elif y>0:
                return 'ES'
            else:
                return 'WS'


class TagReward():
    def __init__(self, rewardParam):
        pass

    def __call__(self, action, state):
        robotState = state[state.index('r')+1:state.index('r')+6]
        if state[state.index('n')+1:]=='tagged':
            opponentState = 'tagged'
        else:
            opponentState = state[state.index('n')+1:state.index('n')+6]

        if action == 'Tag':
            if robotState == opponentState:
                return 10.0
            else:
                return -10.0
        else:
            return -1.0



class TagObservation():
    def __init__(self, observationParam):
        pass

    def __call__(self, action, state, observation):
        robotState = state[state.index('r') + 1:state.index('r') + 6]
        if robotState == observation:
            return 1.0
        else:
            return 0.0
