from src.tigermodel import TigerModel
from src.pbvi import PBVI
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
        'expend_N': 1,
        'expend_method': 'SSRA',    # RA, SSRA, SSEA
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

    # initialize environment
    modelEnv = TigerModel()
    modelEnv.specifyEnvironmentArguments(envParams)
    
    # initialize solver
    solver = PBVI(modelEnv)
    beliefPoints = modelEnv.generateInitBeliefPoints(algoParams['num_belief'])
    solver.specifyAlgorithmArguments(beliefPoints,algoParams)
    
    # initialize visualization tools
    #visualizer= VisualizedTiger()
    #visualizer.visualizeBeliefPoint(beliefPoints)

    totalRewards = 0
    belief = modelEnv.generateUniformBeliefs()    # for model evaluation
    if execParams['print_process']:
        print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
            '''.format(modelEnv.currentState,belief,algoParams['horizon_T'],execParams['max_play']))
    
    # start playing
    starttime = datetime.datetime.now()
    for i in range(execParams['max_play']):
        # this is a general framework of solving POMDP problems
        state = modelEnv.currentState
        action = solver.getPlanningAction(state, belief)       # get best action
        nextState, observation, reward = modelEnv.envFeedback(state, action)  # receive environment feedback
        belief = modelEnv.updateBelief(belief, action, observation)    # update the belief
        totalRewards += reward
        modelEnv.currentState = nextState
        # for every trial, print the result
        if execParams['print_process']:
            print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
    # end playing
    endtime = datetime.datetime.now()
    
    print("Total reward:{}".format(totalRewards))
    print("Playing time:  {} sec".format(round((endtime - starttime).seconds+0.000001*(endtime - starttime).microseconds,2)))


if __name__ == '__main__':
    main()
