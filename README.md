## Goal of this project

Code a basic agent in Python.

Consider a 1d simulation with the position of a ball x(t).

Goal of AI: within time span [0, T] move the ball into a *goal area* x \in [x0, x1]. 

So that the problem is non-trivial, the agent can only apply a force to update the position. Therefore, in order to reach the goal the agent must start braking ahead of time.

By also adding a penalty for time spent reaching the goal, the agent should try to reach it as fast as possible, *without* overshooting.

Accordingly, the agent has two constraints:
1. Be in the target area before t=T.
2. Minimize time t taken to reach target area. The penalty is calculated as which percentage of T was the ball outside the goal.

The Agent now looks at position, velocity, current acceleration, time and goal position and does:
1. x = agent.predict_value()
2. simulation.accelerate(x)

Note that acceleration values are truncated at +/- sim.max_acceleration to ensure stability. Default 5.