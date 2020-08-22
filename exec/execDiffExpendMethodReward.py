from src.tigermodel import TigerModel
from src.pbvi import PBVI

from src.pbviBeliefExpansion import BeliefExpension
from src.pomdpSimulation import  POMDP
from visualization.visualizeTiger import VisualizedTiger

import numpy as np

def main():
    for e in ['RA','SSRA','SSEA']:
        execParams = {
            'model_name': 'Tiger',
            'max_play': 100,
            'print_process': False,
        }
        algoParams = {
            'algo':'pbvi',
            'horizon_T': 20,
            'expend_N': 1,            # notice: here's 1
            'expend_method': e,
            'num_belief': 1,        # inital belief = 1
        }
        envParams = {
            'env_name': 'Tiger_env',
            'discount': 0.75,
            'reward_param': {
                'open_correct_reward': 10.,
                'open_incorrect_cost': -100.,
                'listen_cost': -1.,
            },
            'observation_param': {
                'obs_correct_prob': 0.85,
                'obs_incorrect_prob': 0.15,
            }
        }




        Gen = 50
        Trial = 10
        horizonReward = [0]*Gen

        for trial in range(Trial):
            modelEnv = TigerModel()
            modelEnv.specifyEnvironmentArguments(envParams)
            pomdp = POMDP(modelEnv)

            # initial belief points for PBVI
            beliefPoints = modelEnv.generateInitBeliefPoints(algoParams['num_belief'])

            if algoParams['expend_method'] == 'RA':
                beliefExpendMethod = BeliefExpension(modelEnv).randomBeliefSelection
            elif algoParams['expend_method'] == 'SSRA':
                beliefExpendMethod = BeliefExpension(modelEnv).simulationWithRandomAction
            elif algoParams['expend_method'] == 'SSEA':
                beliefExpendMethod = BeliefExpension(modelEnv).simulationWithExploratoryAction

            numBeliefPoint = []

            for gen in range(50):
                # initialize part
                solver = PBVI(modelEnv)
                solver.specifyAlgorithmArguments(beliefPoints, algoParams)
                totalRewards = 0
                belief = modelEnv.generateUniformBeliefs()

                # model evaluation
                for i in range(execParams['max_play']):
                    # this is a general framework of solving POMDP problems
                    state = modelEnv.currentState
                    action = solver.getPlanningAction(belief)  # get best action
                    nextState, observation, reward = pomdp.envFeedback(state, action)  # receive environment feedback
                    belief = pomdp.updateBelief(belief, action, observation)  # update the belief
                    totalRewards += reward
                    modelEnv.currentState = nextState
                    # for every trial, print the result
                    if execParams['print_process']:
                        print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
                #print("Total reward:{}".format(totalRewards))
                horizonReward[gen]+=round(totalRewards/Trial,2)
                numBeliefPoint.append(gen+1)

                # expend the belief for testing
                beliefPoints = beliefExpendMethod(beliefPoints)

        print("#method=",e)
        print("#r=",horizonReward)
        print("#t=",numBeliefPoint)


if __name__ == '__main__':
    main()
