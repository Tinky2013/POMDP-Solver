# POMDP Solver

***

Here's the code base of algorthm that can solve POMDPs, for example, PBVI (Point Based Value Iteration). The project will continuously update.

**File Organization**

* [**runPomdpExample.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/runPomdpExample.py): Executable example.

* src
  * [**pomdpSimulation.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/pomdpSimulation.py): Simulate the POMDP world (For model evaluation part).
  * [**pbvi.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/pbvi.py): Core code of PBVI (Point Based Value Iteration).
  * [**pbviBeliefExpension.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/pbviBeliefExpansion.py): Belief Expension Method for PBVI.
  * [**tigermodel.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/tigermodel.py): Tiger Model example.
  * [**tagmodel.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/tagmodel.py): Tag Model example.

* Environment
  * [**tigerEnvironment.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/Environment/tigerEnvironment.py): Task Environment of Two-Tiger Problem.
  * [**tagEnvironment.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/Environment/tagEnvironment.py): Task Environment of Tag Problem.
  
* tools: Useful packed tools for solving POMDPs.
  * [**alphaVector.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/tools/alphaVector.py): Alpha-Vector data structure.
  * [**sampleUtility.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/tools/sampleUtility.py): Sampling method packages.

* exec: Model evaluation for different conditions (different parameter settings).

* visualization
  * [**visualizeTiger.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/visualization/visualizeTiger.py): Visualize tiger model structure.
  * visualizeExec: Visualize the evaluation results.
