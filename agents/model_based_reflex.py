from agents.base import BaseAgent
import numpy as np


class ModelBasedReflexAgent(BaseAgent):

    def __init__(self):
        super().__init__()


    def act(self, state):

        x = state['x']
        v = state['v']
        a = state['a']
        max_a = state['max_acceleration']
        goal_min = state['goal_min']
        goal_max = state['goal_max']

        goal_center = 0.5 * (goal_max + goal_min)

        if goal_min <= x <= goal_max:
            if np.abs(v) < 1e-6:
                set_a = 0
                return set_a

        if a == 0:
            if not goal_min <= x <= goal_max:
                set_a = max_a * np.sign(x - goal_center)
        else:
            stopping_distance = np.abs((v ** 2) / (2 * a))

            delta_x = np.abs(x - goal_center)
            direction = np.sign(v)

            if delta_x < stopping_distance:
                set_a = -max_a * direction
            else:
                set_a = max_a * direction

        return set_a
