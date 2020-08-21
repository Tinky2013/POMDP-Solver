from src.tagmodel import TagModel
from src.pbvi import PBVI
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
        'num_belief': 1,
    }
    envParams = {
        'env_name': 'Tag_env',
        'discount': 0.75,
    }

    # initialize environment
    modelEnv = TagModel()
    modelEnv.specifyEnvironmentArguments(envParams)

    # initialize solver
    solver = PBVI(modelEnv)
    beliefPoints = modelEnv.generateInitBeliefPoints(algoParams['num_belief'])
    solver.specifyAlgorithmArguments(beliefPoints, algoParams)

    totalRewards = 0
    belief = modelEnv.generateUniformBeliefs()  # for model evaluation
    if execParams['print_process']:
        print('''Initial State: {} || Time Horizon: {} || Max Play: {} || Initial Belief: {} 
            '''.format(modelEnv.currentState, algoParams['horizon_T'], execParams['max_play'], belief))

    # start playing
    starttime = datetime.datetime.now()
    for i in range(execParams['max_play']):
        # this is a general framework of solving POMDP problems
        state = modelEnv.currentState
        action = solver.getPlanningAction(state, belief)  # get best action
        nextState, observation, reward = modelEnv.envFeedback(state, action)  # receive environment feedback
        print("The env feedback. nextState: ", nextState, " observation: ", observation)
        belief = modelEnv.updateBelief(state, nextState, belief, action, observation)  # update the belief
        totalRewards += reward
        if 'tag' in nextState:
            break
        modelEnv.currentState = nextState

        # for every trial, print the result
        if execParams['print_process']:
            print(
                "Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(
                    i, action, observation, reward, nextState, belief))
        print("---------")
    # end playing
    endtime = datetime.datetime.now()

    print("Total reward:{}".format(totalRewards))
    print("Playing time:  {} sec".format(
        round((endtime - starttime).seconds + 0.000001 * (endtime - starttime).microseconds, 2)))


if __name__ == '__main__':
    main()
