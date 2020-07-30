from src.tigermodel import TigerModel
from src.pbvi import PBVI

def main():
    execParams = {
        'config': 'pbvi',
        'model_name': 'Tiger',
        'max_play': 100,
    }

    algoParams = {
        'algo':'pbvi',
        'T': 5,
    }

    modelName = execParams['model_name']
    maxPlay = execParams['max_play']
    algoName = algoParams['algo']
    horizonT = algoParams['T']
    modelEnv = None     # model environment
    solve = None        # solver

    print("Initialising-------------")

    # here we choose the task environment and the solver
    if modelName == 'Tiger':
        modelEnv = TigerModel()
    if algoName == 'pbvi':
        solve = PBVI()


    # here we generate the initial belief
    belief = modelEnv.generateUniformBeliefs()
    totalRewards = 0

    print('''
    *************************
    Initial State:   {}
    Initial Belief:  {}
    Time Horizon:    {}
    Max Play:        {}
    *************************
    '''.format(modelEnv.currentState,belief,horizonT,maxPlay))

    # start playing
    for i in range(maxPlay):
        # TODO: write the main part of the solving
        pass


if __name__ == '__main__':
    main()
