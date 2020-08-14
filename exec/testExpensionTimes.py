from src.tigermodel import TigerModel
from src.pbvi import PBVI

from tools.sampleUtility import generateInitBeliefPoints, generateUniformBeliefs
import datetime
import numpy as np
from src.pbviBeliefExpansion import BeliefExpension

def main():
    execParams = {
        'model_name': 'Tiger',
        'max_play': 100,
        'print_process': False,
    }
    algoParams = {
        'algo':'pbvi',
        'horizon_T': 10,
        'expend_N': 1,              # when testing generation times, expend_N should be 1
        'expend_method': 'SSEA',    # RA, SSRA, SSEA
        'step_size': 0.6,           # two initial belief points (tiger problem is really small scale)
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


    modelEnv = TigerModel()
    modelEnv.specifyEnvironmentArguments(envParams)
    # initial belief points for PBVI
    beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['step_size'])
    print(len(beliefPoints))
    starttime = datetime.datetime.now()

    timeRecord = []
    rewardRecord = []
    for gen in range(200):
        # more belief points, more accurate solution
        beliefExpension = BeliefExpension(modelEnv)
        beliefExpendMethod = beliefExpension.simulationWithExploratoryAction
        for newP in range(1):  # how much new belief points we generate each time
            beliefPoints = beliefExpendMethod(beliefPoints)


        solver = PBVI(modelEnv)
        solver.specifyAlgorithmArguments(beliefPoints,algoParams)
        totalRewards = 0
        belief = generateUniformBeliefs(modelEnv.states)    # for model evaluation
        if execParams['print_process']:
            print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
                '''.format(modelEnv.currentState,belief,algoParams['horizon_T'],execParams['max_play']))

        # 100-play process
        for i in range(execParams['max_play']):
            # this is a general framework of solving POMDP problems
            action = solver.getPlanningAction(belief)       # get best action
            nextState, observation, reward = modelEnv.envFeedback(action)  # receive environment feedback
            belief = modelEnv.updateBelief(belief, action, observation)    # update the belief
            totalRewards += reward
            # for every trial, print the result
            if execParams['print_process']:
                print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
        print("Total reward:{}".format(totalRewards))
        rewardRecord.append(totalRewards)

        # record the playing time
        endtime = datetime.datetime.now()
        timeFloat = round((endtime - starttime).seconds+0.000001*(endtime - starttime).microseconds,2)
        print("Playing time:  {} sec".format(timeFloat))
        print("------------------------------")
        timeRecord.append(timeFloat)

    # print result
    print("reward_record:",rewardRecord)
    print("time_record:",timeRecord)


if __name__ == '__main__':
    main()
