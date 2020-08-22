from src.tigermodel import TigerModel
from src.pbvi import PBVI
from visualization.visualizeTiger import VisualizedTiger
from src.pomdpSimulation import  POMDP

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
    pomdp = POMDP(modelEnv)
    
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
    for i in range(execParams['max_play']):
        # this is a general framework of solving POMDP problems
        state = modelEnv.currentState
        action = solver.getPlanningAction(belief)       # get best action
        nextState, observation, reward = pomdp.envFeedback(state, action)  # receive environment feedback
        belief = pomdp.updateBelief(belief, action, observation)    # update the belief
        totalRewards += reward
        modelEnv.currentState = nextState
        # for every trial, print the result
        if execParams['print_process']:
            print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))

    print("Total reward:{}".format(totalRewards))

if __name__ == '__main__':
    main()
