
class TagTransition():
    def __init__(self):
        self.worldMap = {
            '[1,5]': 'mainland', '[1,6]': 'mainland', '[1,7]': 'mainland', '[2,6]': 'mainland', '[3,6]': 'mainland',
            '[1,1]': 'north edge', '[1,2]': 'north edge', '[1,3]': 'north edge', '[1,4]': 'north edge',
            '[1,8]': 'north edge', '[4,6]': 'north edge',
            '[0,1]': 'south edge', '[0,2]': 'south edge', '[0,3]': 'south edge', '[0,4]': 'south edge',
            '[0,5]': 'south edge', '[0,6]': 'south edge', '[0,7]': 'south edge', '[0,8]': 'south edge',
            '[2,5]': 'west edge', '[3,5]': 'west edge',
            '[2,7]': 'east edge', '[3,7]': 'east edge',
            '[1,0]': 'northwest corner', '[4,5]': 'northwest corner',
            '[1,9]': 'northeast corner', '[4,7]': 'northeast corner',
            '[0,0]': 'southwest corner',
            '[0,9]': 'southeast corner',
        }
        self.oppoReactProb = {
            'mainland': {
                'Same Row or Col': 0.8 / 3,
                'robot at northwest': 0.8 / 2, 'robot at northeast': 0.8 / 2,
                'robot at southeast': 0.8 / 2, 'robot at southwest': 0.8 / 2,
            },
            'north edge': {
                'Same Row or Col': 0.8 / 2,
                'robot at northwest': 0.8 / 2, 'robot at northeast': 0.8 / 2,
                'robot at southeast': 0.8 / 1, 'robot at southwest': 0.8 / 1,
            },
            'south edge': {
                'Same Row or Col': 0.8 / 2,
                'robot at northwest': 0.8 / 1, 'robot at northeast': 0.8 / 1,
                'robot at southeast': 0.8 / 2, 'robot at southwest': 0.8 / 2,   # although me may not need this line in this world shape
            },
            'west edge': {
                'Same Row or Col': 0.8 / 2,
                'robot at northwest': 0.8 / 2, 'robot at northeast': 0.8 / 1,
                'robot at southeast': 0.8 / 1, 'robot at southwest': 0.8 / 2,
            },
            'east edge': {
                'Same Row or Col': 0.8 / 2,
                'robot at northwest': 0.8 / 1, 'robot at northeast': 0.8 / 2,
                'robot at southeast': 0.8 / 2, 'robot at southwest': 0.8 / 1,
            },
            'southwest corner': {
                'Same Row or Col': 0.2,
                'robot at northwest': 0.2, 'robot at northeast': 1.0,
                'robot at southeast': 0.2, 'robot at southwest': 0.2,
            },
            'southeast corner': {
                'Same Row or Col': 0.2,
                'robot at northwest': 1.0, 'robot at northeast': 0.2,
                'robot at southeast': 0.2, 'robot at southwest': 0.2,
            },
            'northwest corner': {
                'Same Row or Col': 0.2,
                'robot at northwest': 0.2, 'robot at northeast': 0.2,
                'robot at southeast': 1.0, 'robot at southwest': 0.2,
            },
            'northeast corner': {
                'Same Row or Col': 0.2,
                'robot at northwest': 0.2, 'robot at northeast': 0.2,
                'robot at southeast': 0.2, 'robot at southwest': 1.0,
            },
        }
        self.robotValidAction = {
            'mainland': {'Tag': 1.0, 'North': 1.0, 'South': 1.0, 'West': 1.0, 'East': 1.0,},
            'north edge': {'Tag': 1.0, 'South': 1.0, 'West': 1.0, 'East': 1.0,},
            'south edge': {'Tag': 1.0, 'North': 1.0, 'West': 1.0, 'East': 1.0,},
            'west edge': {'Tag': 1.0, 'North': 1.0, 'South': 1.0, 'East': 1.0,},
            'east edge': {'Tag': 1.0, 'North': 1.0, 'South': 1.0, 'West': 1.0,},
            'southwest corner': {'Tag': 1.0, 'North': 1.0, 'East': 1.0,},
            'southeast corner': {'Tag': 1.0, 'North': 1.0, 'West': 1.0,},
            'northwest corner': {'Tag': 1.0, 'South': 1.0, 'East': 1.0,},
            'northeast corner': {'Tag': 1.0, 'South': 1.0, 'West': 1.0,},
        }
        self.robotValidActionNextstate = {
            'Tag': {(0,0): 1.0},
            'North': {(1,0): 1.0},
            'South': {(-1,0): 1.0},
            'West': {(0,-1): 1.0},
            'East': {(0,1): 1.0},
        }
        self.oppoValidPositionShift = {(0,0): 1.0, (0,1): 1.0, (1,0): 1.0, (0,-1): 1.0, (-1,0): 1.0}
        self.oppoShouldAvoidRobot = {

        }

    def __call__(self, action, state, nextState):
        robotState = state[state.index('r')+1:state.index('r')+6]
        oppoState = state[state.index('n')+1:state.index('n')+6]
        robotNextState = nextState[nextState.index('r')+1:nextState.index('r')+6]
        if nextState[nextState.index('n')+1:]=='tagged':
            oppoNextState = 'tagged'    # game over
            return 1.0
        else:
            oppoNextState = nextState[nextState.index('n')+1:nextState.index('n')+6]


        # ensure the valid input
        isRobotActionValid = self.judgeRobotActionValid(robotState, action)


        isOppoEscaping = self.judgeOppoEscaping(oppoState, oppoNextState)
        whereIsRobot = self.robotIsAt(robotNextState, oppoState)

        oppoNowPosition = self.worldMap.get(oppoState, None)   # str described position

        if robotState==oppoState and action == 'Tag':
            return 1.0    # game over

        elif robotNextState==oppoState and action != 'Tag':
            if isOppoEscaping == False:
                return 0.2
            else:
                if 'corner' in oppoNowPosition:    # oppo at corners
                    return 0.8/2
                elif 'edge' in oppoNowPosition:       # oppo at edges
                    return 0.8/3
                else:                           # oppo at mainland
                    return 0.8/4

        # whether action is tag do not influence the result
        else:
            if isOppoEscaping == True:   # opponent escaping
                # oppo at corner
                if 'corner' in oppoNowPosition:
                    return 0.8
                # oppo not at corner
                else:
                    return self.oppoReactProb[oppoNowPosition].get(whereIsRobot, 0.0)

            else:                     # opponent staying
                # oppo not at corner
                if 'corner' not in oppoNowPosition:
                    return 0.2
                # oppo at corner
                else:
                    return self.oppoReactProb[oppoNowPosition].get(whereIsRobot, 0.0)


    def judgeOppoEscaping(self, oppoState, oppoNextState):
        relativeVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(oppoNextState))))
        if relativeVec == [0,0]:
            return False    # oppo stay
        else:
            return True     # oppo escape

    def robotIsAt(self, robotNextState, oppoState):
        relativeVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(robotNextState))))
        rowVec = relativeVec[0]
        colVec = relativeVec[1]
        if rowVec == 0 or colVec == 0:
            return 'Same Row or Col'
        elif rowVec > 0 and colVec < 0:
            return 'robot at northwest'
        elif rowVec > 0 and colVec > 0:
            return 'robot at northeast'
        elif rowVec < 0 and colVec > 0:
            return 'robot at southeast'
        else:
            return 'robot at southwest'

    def judgeRobotActionValid(self, robotState, action):
        # robot can't go outside the world
        robotPosition = self.worldMap.get(robotState, None)
        return self.robotValidAction[robotPosition].get(action, 0.0)

    def judgeRobotActionNextstateValid(self, robotState, action, robotNextState):
        # for the robot, given its state and action, the nextState is fixed
        directionVec = list(map(lambda v: v[1] - v[0], zip(eval(robotState), eval(robotNextState))))
        return self.robotValidActionNextstate[action].get(tuple(directionVec), 0.0)

    def judgeOppoPositionShiftValid(self, oppoState, oppoNextState):
        # for the opponent, it can only stay or move to the neighbor state
        directionVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(oppoNextState))))
        return self.oppoValidPositionShift.get(tuple(directionVec), 0.0)

    def judgeOppoAvoidRobot(self, robotNextState, oppoState, oppoNextState):
        # the opponent can't move towards the robot (eliminate the white part)
        whereIsRobot = self.robotIsAt(robotNextState, oppoState)
        oppoDirectionVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(oppoNextState))))



class TagReward():
    def __init__(self):
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
    def __init__(self):
        pass

    def __call__(self, action, state, observation):
        robotState = state[state.index('r')+1:state.index('r')+6]
        if state[state.index('n')+1:]=='tagged':
            oppoState = 'tagged'    # game over
        else:
            oppoState = state[state.index('n')+1:state.index('n')+6]

        if action == 'Tag':
            if oppoState == 'tagged' and observation == 'ntagged':
                return 1.0
            else:
                return 1/28 # oppo not in this blog! not tagged!
        else:
            return 1/29 # do not know anything except untagged
