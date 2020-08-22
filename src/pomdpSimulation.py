
from tools.sampleUtility import chooseItemIdx

class POMDP():
    def __init__(self, modelEnv):
        self.states = modelEnv.states
        self.observations = modelEnv.observations

        self.transitionFunction = modelEnv.transitionFunction
        self.rewardFunction = modelEnv.rewardFunction
        self.observationFunction = modelEnv.observationFunction



    def envFeedback(self, state, action):
        # after we have state and action, we can calculate observation, reward, nextState
        nextStateProbs = [self.transitionFunction(action, state, sj) for sj in self.states]
        nextState = self.states[chooseItemIdx(nextStateProbs)]

        observationProbs = [self.observationFunction(action, nextState, oj) for oj in self.observations]
        observation = self.observations[chooseItemIdx(observationProbs)]
        reward = self.rewardFunction(action, state)

        return nextState, observation, reward


    def updateBelief(self, belief, action, observation):
        newBelief = [
            self.observationFunction(action, sj, observation) * sum(
                [self.transitionFunction(action, si, sj) * float(belief[i]) for i, si in enumerate(self.states)]
            ) for sj in self.states
        ]

        # get the normalized belief
        normalizedFactor = sum(newBelief)
        assert (normalizedFactor != 0)
        normalizedBelief = [x / normalizedFactor for x in newBelief]
        return normalizedBelief  # return array with length=stateDim
