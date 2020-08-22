from src.tagmodel import TagModel
from src.pbvi import PBVI
from src.pomdpSimulation import  POMDP


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
        'num_belief': 5,
    }
    envParams = {
        'env_name': 'Tag_env',
        'discount': 0.75,
    }

    # initialize environment
    modelEnv = TagModel()
    modelEnv.specifyEnvironmentArguments(envParams)
    pomdp = POMDP(modelEnv)

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
    for i in range(execParams['max_play']):
        # this is a general framework of solving POMDP problems
        state = modelEnv.currentState
        action = solver.getPlanningAction(belief)  # get best action
        nextState, observation, reward = pomdp.envFeedback(state, action)  # receive environment feedback
        belief = pomdp.updateBelief(belief, action, observation)  # update the belief
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


    print("Total reward:{}".format(totalRewards))


if __name__ == '__main__':
    main()
