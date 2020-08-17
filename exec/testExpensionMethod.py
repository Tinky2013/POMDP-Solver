from src.tigermodel import TigerModel
from src.pbvi import PBVI

from tools.sampleUtility import generateInitBeliefPoints, generateUniformBeliefs
import datetime
import numpy as np
from src.pbviBeliefExpansion import BeliefExpension

def main():
    for method in ['RA','SSRA','SSEA']:
        execParams = {
            'model_name': 'Tiger',
            'max_play': 100,
            'print_process': False,
        }
        algoParams = {
            'algo':'pbvi',
            'horizon_T': 20,
            'expend_N': 1,              # when testing generation times, expend_N should be 1
            'expend_method': method,    # RA, SSRA, SSEA
            'init_num_belief': 1,
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

        repeatRun = 10
        timeRecord = [0] * 100
        rewardRecord = [0] * 100

        for ave in range(repeatRun):
            modelEnv = TigerModel()
            modelEnv.specifyEnvironmentArguments(envParams)
            # initial belief points for PBVI
            beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['init_num_belief'])
            starttime = datetime.datetime.now()
            # more times lopping, more accurate solution
            beliefExpension = BeliefExpension(modelEnv)
            beliefExpendMethod = beliefExpension.simulationWithExploratoryAction


            for gen in range(100):
                # initialize part
                solver = PBVI(modelEnv)
                solver.specifyAlgorithmArguments(beliefPoints,algoParams)
                totalRewards = 0
                belief = generateUniformBeliefs(modelEnv.states)    # for model evaluation
                if execParams['print_process']:
                    print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
                        '''.format(modelEnv.currentState,belief,algoParams['horizon_T'],execParams['max_play']))

                # model evaluation
                for i in range(execParams['max_play']):
                    # this is a general framework of solving POMDP problems
                    action = solver.getPlanningAction(belief)       # get best action
                    nextState, observation, reward = modelEnv.envFeedback(action)  # receive environment feedback
                    belief = modelEnv.updateBelief(belief, action, observation)    # update the belief
                    totalRewards += reward
                    # for every trial, print the result
                    if execParams['print_process']:
                        print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
                #print("Total reward:{}".format(totalRewards))
                rewardRecord[gen]+=round(totalRewards/repeatRun,2)

                # record the playing time
                endtime = datetime.datetime.now()
                timeFloat = round((endtime - starttime).seconds+0.000001*(endtime - starttime).microseconds,2)
                #print("Playing time:  {} sec".format(timeFloat))
                #print("------------------------------")
                timeRecord[gen]+=round(timeFloat/repeatRun,2)

                # expend the belief for testing
                for newP in range(1):  # how much new belief points we generate each time
                    beliefPoints = beliefExpendMethod(beliefPoints)


        # print result
        print("#method=",method)
        print("#r=", rewardRecord)
        print("#runtime=", timeRecord)
        print("#------------------------------")


if __name__ == '__main__':
    main()
