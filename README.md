# POMDP Solver

***

Here's the code base of algorthm that can solve POMDPs, for example, PBVI (Point Based Value Iteration). The project will continuously update.

**File Organization**

* [**runPOMDP.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/runPOMDP.py): Executable File.

* src
  * [**pomdputility.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/pomdputility.py): Super class for all the solvers (although we only implement PBVI now, it will make it easier to add other solvers).
  * [**pbvi.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/pbvi.py): Core code of PBVI (Point Based Value Iteration).
  * [**tigermodel.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/src/tigermodel.py): Model setting part (Receives information from tiger environment).

* Environment
  * [**tigerEnvironment.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/Environment/tigerEnvironment.py): Task Environment of Two-Tiger Problem.
  
* tools: Useful packed tools for solving POMDPs.
  * [**alphaVector.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/tools/alphaVector.py): Alpha-Vector data structure.
  * [**sampleUtility.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/tools/sampleUtility.py): Sampling method packages.

* visualization
  * [**visualizeTiger.py**](https://github.com/Tinky2013/POMDP-Solver/blob/master/visualization/visualizeTiger.py).
