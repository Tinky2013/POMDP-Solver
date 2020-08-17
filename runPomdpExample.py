from src.tigermodel import TigerModel
from src.pbvi import PBVI
from src.pomdputility import EnvFeedback, UpdateBelief

from tools.sampleUtility import generateInitBeliefPoints, generateUniformBeliefs

from visualization.visualizeTiger import VisualizedTiger
import datetime


def main():
    execParams = {
        'model_name': 'Tiger',
        'max_play': 100,
        'print_process': True,
    }
    algoParams = {
        'algo':'pbvi',
        'horizon_T': 10,
        'expend_N': 5,
        'expend_method': 'RA',    # RA, SSRA, SSEA
        'num_belief': 100,
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
    visualizer= VisualizedTiger()
    solver = PBVI(modelEnv)
    envFeedback = EnvFeedback(modelEnv)
    updateBelief = UpdateBelief(modelEnv)

    beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['num_belief'])
    solver.specifyAlgorithmArguments(beliefPoints,algoParams)

    # 5. choose your visualization part
    #visualizer.visualizeBeliefPoint(beliefPoints)


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
        nextState, observation, reward = envFeedback(action)  # receive environment feedback
        belief = updateBelief(belief, action, observation)    # update the belief
        totalRewards += reward

        # for every trial, print the result
        if execParams['print_process']:
            print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
    print("Total reward:{}".format(totalRewards))
    # record the playing time
    endtime = datetime.datetime.now()
    timeFloat = round((endtime - starttime).seconds+0.000001*(endtime - starttime).microseconds,2)
    print("Playing time:  {} sec".format(timeFloat))


if __name__ == '__main__':
    main()
