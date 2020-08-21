from src.tigermodel import TigerModel
from src.pbvi import PBVI
from src.pbviBeliefExpansion import BeliefExpension



def main():
    for h in [1,2,5,10,20,50,100]:
        execParams = {
            'model_name': 'Tiger',
            'max_play': 100,
            'print_process': False,
        }
        algoParams = {
            'algo':'pbvi',
            'horizon_T': h,
            'expend_N': 1,            # notice: here's 1
            'expend_method': 'SSEA',
            'num_belief': 1,        # inital belief = 1
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


        Gen = 50
        Trial = 10
        horizonReward = [0] * Gen

        for trial in range(Trial):
            modelEnv = TigerModel()
            modelEnv.specifyEnvironmentArguments(envParams)

            # initial belief points for PBVI
            beliefPoints = modelEnv.generateInitBeliefPoints(algoParams['num_belief'])
            beliefExpendMethod = BeliefExpension(modelEnv).simulationWithExploratoryAction

            numBeliefPoint = []

            for gen in range(50):
                # initialize part
                pbvi = PBVI(modelEnv)
                pbvi.specifyAlgorithmArguments(beliefPoints, algoParams)
                totalRewards = 0
                belief = modelEnv.generateUniformBeliefs()    # for model evaluation

                # model evaluation
                for i in range(execParams['max_play']):
                    # this is a general framework of solving POMDP problems
                    state = modelEnv.currentState
                    action = pbvi.getPlanningAction(state, belief)  # get best action
                    nextState, observation, reward = modelEnv.envFeedback(state, action)  # receive environment feedback
                    belief = modelEnv.updateBelief(belief, action, observation)  # update the belief
                    totalRewards += reward
                    modelEnv.currentState = nextState

                    # for every trial, print the result
                    if execParams['print_process']:
                        print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
                #print("Total reward:{}".format(totalRewards))
                horizonReward[gen]+=round(totalRewards/Trial,2)
                numBeliefPoint.append(gen+1)

                # expend the belief for testing
                beliefPoints = beliefExpendMethod(beliefPoints)

        print("#horizon=",h)
        print("#r=",horizonReward)
        print("#t=",numBeliefPoint)


if __name__ == '__main__':
    main()
