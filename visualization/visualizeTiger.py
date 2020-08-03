import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
currently this class only applies to Tiger Problem
'''

class VisualizedTiger():
    def __init__(self):
        self.beliefPointsX = []
        self.beliefPointsY = []

    def visualizeBeliefPoint(self, beliefPoints):
        assert(len(beliefPoints[0]!=2))

        for i in beliefPoints:
            summation = i[0]+i[1]
            self.beliefPointsX.append(i[0]/summation)
            self.beliefPointsY.append(i[1]/summation)

        plt.scatter(self.beliefPointsX, [0]*len(self.beliefPointsX))
        plt.show()