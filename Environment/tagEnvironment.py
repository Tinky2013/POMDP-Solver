
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
                'robot here': 0.8 / 4,  'robot at north': 0.8 / 3, 'robot at south': 0.8 / 3, 'robot at west': 0.8 / 3, 'robot at east': 0.8 / 3,
                'robot at northwest': 0.8 / 2, 'robot at northeast': 0.8 / 2,
                'robot at southeast': 0.8 / 2, 'robot at southwest': 0.8 / 2,
            },
            'north edge': {
                'robot here': 0.8 / 3,  'robot at north': 0.8 / 2, 'robot at south': 0.8 / 2, 'robot at west': 0.8 / 2, 'robot at east': 0.8 / 2,
                'robot at northwest': 0.8 / 2, 'robot at northeast': 0.8 / 2,
                'robot at southeast': 0.8 / 1, 'robot at southwest': 0.8 / 1,
            },
            'south edge': {
                'robot here': 0.8 / 3,  'robot at north': 0.8 / 2, 'robot at south': 0.8 / 2, 'robot at west': 0.8 / 2, 'robot at east': 0.8 / 2,
                'robot at northwest': 0.8 / 1, 'robot at northeast': 0.8 / 1,
                'robot at southeast': 0.8 / 2, 'robot at southwest': 0.8 / 2,   # although me may not need this line in this world shape
            },
            'west edge': {
                'robot here': 0.8 / 3,  'robot at north': 0.8 / 2, 'robot at south': 0.8 / 2, 'robot at west': 0.8 / 2, 'robot at east': 0.8 / 2,
                'robot at northwest': 0.8 / 2, 'robot at northeast': 0.8 / 1,
                'robot at southeast': 0.8 / 1, 'robot at southwest': 0.8 / 2,
            },
            'east edge': {
                'robot here': 0.8 / 3,  'robot at north': 0.8 / 2, 'robot at south': 0.8 / 2, 'robot at west': 0.8 / 2, 'robot at east': 0.8 / 2,
                'robot at northwest': 0.8 / 1, 'robot at northeast': 0.8 / 2,
                'robot at southeast': 0.8 / 2, 'robot at southwest': 0.8 / 1,
            },
            'southwest corner': {
                'robot here': 0.4,  'robot at north': 0.2, 'robot at south': 0.2, 'robot at west': 0.2, 'robot at east': 0.2,
                'robot at northwest': 0.2, 'robot at northeast': 1.0,
                'robot at southeast': 0.2, 'robot at southwest': 0.2,
            },
            'southeast corner': {
                'robot here': 0.4,  'robot at north': 0.2, 'robot at south': 0.2, 'robot at west': 0.2, 'robot at east': 0.2,
                'robot at northwest': 1.0, 'robot at northeast': 0.2,
                'robot at southeast': 0.2, 'robot at southwest': 0.2,
            },
            'northwest corner': {
                'robot here': 0.4,  'robot at north': 0.2, 'robot at south': 0.2, 'robot at west': 0.2, 'robot at east': 0.2,
                'robot at northwest': 0.2, 'robot at northeast': 0.2,
                'robot at southeast': 1.0, 'robot at southwest': 0.2,
            },
            'northeast corner': {
                'robot here': 0.4,  'robot at north': 0.2, 'robot at south': 0.2, 'robot at west': 0.2, 'robot at east': 0.2,
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
            'robot here': {(0,0): 1.0, (0,1): 1.0, (1,0): 1.0, (0,-1): 1.0, (-1,0): 1.0},
            'robot at north': {(0,0): 1.0, (0,1): 1.0, (0,-1): 1.0, (-1,0): 1.0},    # don't go north, others equal
            'robot at south': {(0,0): 1.0, (0,1): 1.0, (1,0): 1.0, (0,-1): 1.0},
            'robot at east': {(0,0): 1.0, (1,0): 1.0, (0,-1): 1.0, (-1,0): 1.0},
            'robot at west': {(0,0): 1.0, (0,1): 1.0, (1,0): 1.0, (-1,0): 1.0},
            'robot at northwest': {(0,0): 1.0, (0,1): 1.0, (-1,0): 1.0},
            'robot at northeast': {(0,0): 1.0, (0,-1): 1.0, (-1,0): 1.0},
            'robot at southeast': {(0,0): 1.0, (1,0): 1.0, (0,-1): 1.0},
            'robot at southwest': {(0,0): 1.0, (0,1): 1.0, (1,0): 1.0},
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
        isRobotActionNextstateValid = self.judgeRobotActionNextstateValid(robotState, action, robotNextState)
        isOppoPositionShiftValid = self.judgeOppoPositionShiftValid(oppoState, oppoNextState)
        isOppoAvoidRobot = self.judgeOppoAvoidRobot(robotNextState, oppoState, oppoNextState)
        isValidInput = isRobotActionValid * isRobotActionNextstateValid * isOppoPositionShiftValid * isOppoAvoidRobot
        if isValidInput == 0:
            return 0.0


        isOppoEscaping = self.judgeOppoEscaping(oppoState, oppoNextState)   # judge oppo moving/staying
        whereIsRobot = self.theRobotIsAt(robotNextState, oppoState)            # fixed oppo, where's the robot
        oppoNowPosition = self.worldMap.get(oppoState, None)                # the place of oppo on the world map

        # three situations
        # reach the same blog and tag, game over
        if robotState==oppoState and action == 'Tag':
            return 1.0
        # reach the same blog but did not tag
        elif robotNextState==oppoState and action != 'Tag':
            return 0.2 if (isOppoEscaping == False) else self.oppoReactProb[oppoNowPosition].get(whereIsRobot, 0.0)
        # other conditions
        else:
            # opponent escaping
            if isOppoEscaping == True:
                return 0.8 if ('corner' in oppoNowPosition) else self.oppoReactProb[oppoNowPosition].get(whereIsRobot, 0.0)
            # opponent staying
            else:
                # whether oppo is at corner
                return 0.2 if ('corner' not in oppoNowPosition) else self.oppoReactProb[oppoNowPosition].get(whereIsRobot, 0.0)


    def judgeOppoEscaping(self, oppoState, oppoNextState):
        relativeVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(oppoNextState))))
        return False if (relativeVec == [0,0]) else True

    def theRobotIsAt(self, robotNextState, oppoState):
        relativeVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(robotNextState))))
        rowVec = relativeVec[0]
        colVec = relativeVec[1]
        if rowVec == 0 and colVec == 0:
            return 'robot here'
        elif rowVec > 0 and colVec == 0:
            return 'robot at north'
        elif rowVec < 0 and colVec == 0:
            return 'robot at south'
        elif rowVec == 0 and colVec > 0:
            return 'robot at east'
        elif rowVec == 0 and colVec < 0:
            return 'robot at west'
        elif rowVec > 0 and colVec < 0:
            return 'robot at northwest'
        elif rowVec > 0 and colVec > 0:
            return 'robot at northeast'
        elif rowVec < 0 and colVec > 0:
            return 'robot at southeast'
        else:
            return 'robot at southwest'

    def judgeRobotActionValid(self, robotState, action):
        # robot can't go outside the world (some action can't be chosen)
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
        whereIsRobot = self.theRobotIsAt(robotNextState, oppoState)
        oppoDirectionVec = list(map(lambda v: v[1] - v[0], zip(eval(oppoState), eval(oppoNextState))))
        return self.oppoShouldAvoidRobot[whereIsRobot].get(tuple(oppoDirectionVec), 0.0)


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
            return 10.0 if (robotState == opponentState) else -10.0
        else:
            return -1.0



class TagObservation():
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
        self.robotValidNewPosition = {
            'mainland': {'Tag': 1.0, 'North': 1.0, 'South': 1.0, 'West': 1.0, 'East': 1.0,},
            'north edge': {'Tag': 1.0, 'North': 1.0, 'West': 1.0, 'East': 1.0,},    # previous action can't be 'South'
            'south edge': {'Tag': 1.0, 'South': 1.0, 'West': 1.0, 'East': 1.0,},
            'west edge': {'Tag': 1.0, 'North': 1.0, 'South': 1.0, 'West': 1.0,},
            'east edge': {'Tag': 1.0, 'North': 1.0, 'South': 1.0, 'East': 1.0,},
            'southwest corner': {'Tag': 1.0, 'South': 1.0, 'West': 1.0,},
            'southeast corner': {'Tag': 1.0, 'South': 1.0, 'East': 1.0,},
            'northwest corner': {'Tag': 1.0, 'North': 1.0, 'West': 1.0,},
            'northeast corner': {'Tag': 1.0, 'North': 1.0, 'East': 1.0,},
        }

    def __call__(self, action, state, observation):
        # given the action and the physical state that action induced, the observation is fixed
        robotState = state[state.index('r') + 1:state.index('r') + 6]
        if state[state.index('n')+1:]=='tagged':
            oppoState = 'tagged'    # game over
        else:
            oppoState = state[state.index('n')+1:state.index('n')+6]

        robotActionStateValid = self.judgeRobotActionStateValid(robotState, action)
        actionOppoStateValid = self.judgeActionOppoStateValid(oppoState, action)
        actionObservationValid = self.judgeActionObservationValid(action, robotState, oppoState, observation)
        isInputValid = robotActionStateValid * actionOppoStateValid * actionObservationValid
        if isInputValid == 0:
            return 0.0

        return 1.0

    def judgeRobotActionStateValid(self, robotState, action):
        # for the robot, given its action, some state can't reached
        # exp: 'North' can not reach '[0,6]'
        robotNewPosition = self.worldMap.get(robotState, None)
        return self.robotValidNewPosition[robotNewPosition].get(action, 0.0)

    def judgeActionOppoStateValid(self, oppoState, action):
        # for the opponent, given the robot action, some state can't reached
        if oppoState == 'tagged':
            if action != 'Tag':
                return 0.0
        return 1.0

    def judgeActionObservationValid(self, action, robotState, oppoState, observation):
        # given an action and the state it induced, the observation is fixed
        if action == 'Tag':
            return 1.0 if (
                    (oppoState == 'tagged' and observation == 'sameblog')
                    or (oppoState != 'tagged' and observation == ('r'+robotState) and observation != 'sameblog')
            ) else 0.0
        else:
            return 1.0 if (
                    (robotState == oppoState and observation == 'sameblog')
                    or (robotState != oppoState and observation == ('r'+robotState))
            ) else 0.0


