from src.tigermodel import TigerModel
from src.pbvi import PBVI

from tools.sampleUtility import generateBeliefPoints, generateUniformBeliefs

from visualization.visualizeTiger import VisualizedTiger

def main():
    execParams = {
        'config': 'pbvi',
        'model_name': 'Tiger',
        'max_play': 100,

        'print_process': True,
    }
    algoParams = {
        'algo':'pbvi',
        'T': 5,
        'step_size': 0.01,
    }

    modelName = execParams['model_name']
    maxPlay = execParams['max_play']
    algoName = algoParams['algo']
    horizonT = algoParams['T']
    modelEnv = None     # model environment
    solver = None        # solver
    visualizer = None

    print("Initialising...")

    # here we choose the task environment and the solver
    if modelName == 'Tiger':
        modelEnv = TigerModel()
        visualizer= VisualizedTiger()
    if algoName == 'pbvi':
        solver = PBVI(modelEnv)

    # here we generate the initial belief and choose some belief points
    belief = generateUniformBeliefs(modelEnv.states)        # initial belief: [0.5,0.5]
    beliefPoints = generateBeliefPoints(modelEnv.states, algoParams['step_size'])
    solver.specifyAlgorithmArguments(beliefPoints)


    #visualizer.visualizeBeliefPoint(beliefPoints)

    totalRewards = 0
    if execParams['print_process']:
        print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
        '''.format(modelEnv.currentState,belief,horizonT,maxPlay))



    # start playing
    for i in range(maxPlay):
        # this is a general framework of solving POMDP problems
        solver.planningHorizon(horizonT)                               # planning
        action = solver.getBestAction(belief)                        # get best action
        nextState, observation, reward = solver.envFeedback(action)  # receive environment feedback
        belief = solver.updateBelief(belief, action, observation)    # update the belief
        totalRewards += reward

        # for every trial, print the result
        if execParams['print_process']:
            print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))

    print("Total reward:{}".format(totalRewards))



if __name__ == '__main__':
    main()
