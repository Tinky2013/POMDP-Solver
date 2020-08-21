from src.tigermodel import TigerModel
from src.pbvi import PBVI
import datetime


def main():
    for b in [2,5,10,20,50,100]:
        timeRecord = []
        for h in [10,20,30,40,50,60,70,80,90,100]:
            execParams = {
                'model_name': 'Tiger',
                'max_play': 100,
                'print_process': False,
            }
            algoParams = {
                'algo':'pbvi',
                'horizon_T': h,
                'expend_N': 1,
                'expend_method': 'RA',    # RA, SSRA, SSEA
                'num_belief': b,
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
            solver = PBVI(modelEnv)

            beliefPoints = modelEnv.generateInitBeliefPoints(algoParams['num_belief'])
            solver.specifyAlgorithmArguments(beliefPoints,algoParams)

            # start playing
            totalRewards = 0
            belief = modelEnv.generateUniformBeliefs()    # for model evaluation
            if execParams['print_process']:
                print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
                    '''.format(modelEnv.currentState,belief,algoParams['horizon_T'],execParams['max_play']))


            starttime = datetime.datetime.now()
            # only planning process
            state = modelEnv.currentState
            action = solver.getPlanningAction(state, belief)
            # record the playing time
            endtime = datetime.datetime.now()
            timeFloat = round((endtime - starttime).seconds+0.000001*(endtime - starttime).microseconds,2)
            #print("Playing time:  {} sec".format(timeFloat))
            timeRecord.append(timeFloat)

        print("#numBelief=",b)
        print("#p=",timeRecord)


if __name__ == '__main__':
    main()
