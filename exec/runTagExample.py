from src.tagmodel import TagModel
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
        'algo': 'pbvi',
        'horizon_T': 1,
        'expend_N': 1,
        'expend_method': 'SSRA',  # RA, SSRA, SSEA
        'num_belief': 1000,
    }
    envParams = {
        'env_name': 'Tag_env',
        'discount': 0.75,
    }

    # initialize environment
    modelEnv = TagModel()
    modelEnv.specifyEnvironmentArguments(envParams)
    envFeedback = EnvFeedback(modelEnv)
    updateBelief = UpdateBelief(modelEnv)

    # initialize solver
    solver = PBVI(modelEnv)
    beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['num_belief'])
    solver.specifyAlgorithmArguments(beliefPoints, algoParams)

    totalRewards = 0
    belief = generateUniformBeliefs(modelEnv.states)  # for model evaluation
    if execParams['print_process']:
        print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
            '''.format(modelEnv.currentState, belief, algoParams['horizon_T'], execParams['max_play']))

    # start playing
    starttime = datetime.datetime.now()
    for i in range(execParams['max_play']):
        # this is a general framework of solving POMDP problems
        action = solver.getPlanningAction(belief)  # get best action
        nextState, observation, reward = envFeedback(action)  # receive environment feedback
        belief = updateBelief(belief, action, observation)  # update the belief
        totalRewards += reward
        # for every trial, print the result
        if execParams['print_process']:
            print(
                "Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(
                    i, action, observation, reward, nextState, belief))
    # end playing
    endtime = datetime.datetime.now()

    print("Total reward:{}".format(totalRewards))
    print("Playing time:  {} sec".format(
        round((endtime - starttime).seconds + 0.000001 * (endtime - starttime).microseconds, 2)))


if __name__ == '__main__':
    main()
