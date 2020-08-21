import numpy as np
import random
from array import array
from numpy import *

np.random.seed()
random.seed()

def chooseItemIdx(probs):
    assert(abs(sum(probs) - 1.0) <= 0.00000000000000)
    probs = np.array(probs)
    return np.random.choice(list(range(len(probs))), p=probs/probs.sum())

def distanceL1(u,v):
    assert(len(u)==len(v))
    return sum(list(map(lambda x,y:abs(x-y), u, v)))
