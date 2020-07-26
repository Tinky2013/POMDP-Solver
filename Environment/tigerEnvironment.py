class TigerTransition():
    def __init__(self):
        self.transitionMatrix = {
            ('listen', 'tiger-left', 'tiger-left'): 1.0,
            ('listen', 'tiger-left', 'tiger-right'): 0.0,
            ('listen', 'tiger-right', 'tiger-left'): 0.0,
            ('listen', 'tiger-right', 'tiger-right'): 1.0,

            ('open-left', 'tiger-left', 'tiger-left'): 0.5,
            ('open-left', 'tiger-left', 'tiger-right'): 0.5,
            ('open-left', 'tiger-right', 'tiger-left'): 0.5,
            ('open-left', 'tiger-right', 'tiger-right'): 0.5,

            ('open-right', 'tiger-left', 'tiger-left'): 0.5,
            ('open-right', 'tiger-left', 'tiger-right'): 0.5,
            ('open-right', 'tiger-right', 'tiger-left'): 0.5,
            ('open-right', 'tiger-right', 'tiger-right'): 0.5
        }

    def __call__(self, action, state, nextState):
        nextStateProb = self.transitionMatrix.get((action, state, nextState), 0.0)
        return nextStateProb

class TigerReward():
    def __init__(self):
        self.rewardMatrix = {
            ('listen', 'tiger-left'): -1.0,
            ('listen', 'tiger-right'): -1.0,

            ('open-left', 'tiger-left'): -100.0,
            ('open-left', 'tiger-right'): 10.0,

            ('open-right', 'tiger-left'): 10.0,
            ('open-right', 'tiger-right'): -100.0
        }

    def __call__(self, action, state):
        rewardFixed = self.rewardMatrix.get((action, state), 0.0)
        return rewardFixed

class TigerObservation():
    def __init__(self):
        self.observationMatrix = {
            ('listen', 'tiger-left', 'tiger-left'): 0.85,
            ('listen', 'tiger-left', 'tiger-right'): 0.15,
            ('listen', 'tiger-right', 'tiger-left'): 0.15,
            ('listen', 'tiger-right', 'tiger-right'): 0.85,

            ('open-left', 'tiger-left', 'tiger-left'): 0.5,
            ('open-left', 'tiger-left', 'tiger-right'): 0.5,
            ('open-left', 'tiger-right', 'tiger-left'): 0.5,
            ('open-left', 'tiger-right', 'tiger-right'): 0.5,

            ('open-right', 'tiger-left', 'tiger-left'): 0.5,
            ('open-right', 'tiger-left', 'tiger-right'): 0.5,
            ('open-right', 'tiger-right', 'tiger-left'): 0.5,
            ('open-right', 'tiger-right', 'tiger-right'): 0.5
        }

    def __call__(self, action, state, observation):
        observationProb = self.observationMatrix.get((action, state, observation), 0.0)
        return observationProb
