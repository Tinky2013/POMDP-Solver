'''
This file is a wrapper for alpha vector
The alpha vector can represent the value function
'''
class AlphaVector(object):
    def __init__(self, action, value):
        self.action = action
        self.value = value

    def usingAlphaVector(self):
        return AlphaVector(self.action, self.value)