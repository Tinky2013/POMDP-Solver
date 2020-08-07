from src.tigermodel import TigerModel
from src.pbvi import PBVI

from tools.sampleUtility import generateBeliefPoints, generateUniformBeliefs

from visualization.visualizeTiger import VisualizedTiger

def main():
    # 1. choose your parameters
    execParams = {
        'config': 'pbvi',
        'model_name': 'Tiger',
        'max_play': 100,

        'print_process': True,
    }
    algoParams = {
        'algo':'pbvi',
        'T': 2,
        'expend': 5,
        'step_size': 0.01,
    }

    modelName = execParams['model_name']
    maxPlay = execParams['max_play']
    algoName = algoParams['algo']
    horizonT = algoParams['T']
    expendN = algoParams['expend']
    modelEnv = None     # model environment
    solver = None        # solver
    visualizer = None

    # 2. choose your environment
    if modelName == 'Tiger':
        modelEnv = TigerModel()
        visualizer= VisualizedTiger()
    else:
        pass

    # 3. choose your solver
    if algoName == 'pbvi':
        solver = PBVI(modelEnv)
    else:
        pass

    # 4. choose your belief generation method
    belief = generateUniformBeliefs(modelEnv.states)        # initial belief: [0.5,0.5]
    beliefPoints = generateBeliefPoints(modelEnv.states, algoParams['step_size'])
    solver.specifyAlgorithmArguments(beliefPoints,expendN)

    # 5. choose your visualization part
    #visualizer.visualizeBeliefPoint(beliefPoints)


    # start playing
    totalRewards = 0
    if execParams['print_process']:
        print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
        '''.format(modelEnv.currentState,belief,horizonT,maxPlay))
    for i in range(maxPlay):
        # this is a general framework of solving POMDP problems
        solver.planningHorizon(horizonT)                               # planning
        action = solver.getBestPlanningAction(belief)                        # get best action
        nextState, observation, reward = solver.envFeedback(action)  # receive environment feedback
        belief = solver.updateBelief(belief, action, observation)    # update the belief
        totalRewards += reward
        # for every trial, print the result
        if execParams['print_process']:
            print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
    print("Total reward:{}".format(totalRewards))



if __name__ == '__main__':
    main()
