import unittest
from ddt import ddt,data,unpack
from Environment.tigerEnvironment import TigerTransition, TigerReward, TigerObservation

from src.pbvi import PBVI

import sys
sys.path.append("..")

param = None
pbvi = PBVI(param)

a=pbvi.specifyAlgorithmArguments()
print(a)
