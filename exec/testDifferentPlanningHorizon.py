from src.tigermodel import TigerModel
from src.pbvi import PBVI

from tools.sampleUtility import generateInitBeliefPoints, generateUniformBeliefs
import datetime
import numpy as np


def main():
    for h in [1,2,5,10,20,50,100]:
        execParams = {
            'model_name': 'Tiger',
            'max_play': 100,
            'print_process': False,
        }
        algoParams = {
            'algo':'pbvi',
            'horizon_T': h,
            'expend_N': 5,
            'expend_method': 'SSEA',    # RA, SSRA, SSEA
            'step_size': 0.01,
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

        # 10 repeat test
        TotalReward = []
        TimeFloat = []
        for i in range(10):
            modelEnv = TigerModel()
            modelEnv.specifyEnvironmentArguments(envParams)
            solver = PBVI(modelEnv)

            beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['step_size'])
            solver.specifyAlgorithmArguments(beliefPoints,algoParams)

            # start playing
            totalRewards = 0
            belief = generateUniformBeliefs(modelEnv.states)    # for model evaluation
            if execParams['print_process']:
                print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
                    '''.format(modelEnv.currentState,belief,algoParams['horizon_T'],execParams['max_play']))
            starttime = datetime.datetime.now()

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
            TotalReward.append(totalRewards)

            # record the playing time
            endtime = datetime.datetime.now()
            timeFloat = round((endtime - starttime).seconds+0.000001*(endtime - starttime).microseconds,2)
            #print("Playing time:  {} sec".format(timeFloat))
            TimeFloat.append(timeFloat)

        # print 10 times testing result
        print("planning horizons:{}",algoParams['horizon_T'])
        #print("TotalReward:",TotalReward)
        #print("RunTime:",TimeFloat)
        print("TotalReward_Ave:{}, TotalReward_Std:{}".format(np.mean(TotalReward),round(float(np.std(TotalReward)),2)))
        print("RunTime_Ave:{}, RunTime_Std:{}".format(np.mean(TimeFloat),round(float(np.std(TimeFloat)),2)))
        print("------------------------------")


if __name__ == '__main__':
    main()
