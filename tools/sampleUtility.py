import numpy as np
import random
from array import array
from numpy import *

np.random.seed()
random.seed()

def chooseItemIdx(probs):
    assert(abs(sum(probs) - 1.0) <= 0.0000000)
    probs = np.array(probs)
    return np.random.choice(list(range(len(probs))), p=probs/probs.sum())

def generateBeliefPoints(states, stepsize):
    '''
    Here we used uniform random over the belief simplex
    '''
    beliefPoints = [
        [random.uniform() for s in states] for i in arange(0, 1+stepsize, stepsize)
    ]
    return array(beliefPoints)

def generateUniformBeliefs(states):
    stateNUM = len(states)
    Beliefs = [1/stateNUM for i in range(stateNUM)]
    return Beliefs
