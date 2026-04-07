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
        stopping_distance = np.abs((v ** 2) / (2 * max_a))

        if goal_min <= x <= goal_max:
            if np.abs(v) < 1e-6:
                set_a = 0
                return set_a

        if goal_min <= x <= goal_max:
            if a == 0:
                set_a = 0
            else:
                set_a = -max_a * np.sign(v)
        elif np.abs(x - goal_center) > stopping_distance:
            set_a = -max_a * np.sign(x - goal_center)
        else:
            if np.sign(v) == -np.sign(x - goal_center):
                set_a = -max_a * np.sign(v)
            else:
                set_a = max_a * np.sign(v)

        return set_a