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
        goal_center = state['goal_center'][-1]  # take only current center
        goal_width = state['goal_width'][-1]

        in_goal = (goal_center - goal_width / 2 <= x <= goal_center + goal_width / 2)

        if in_goal:
            if np.abs(v) < 1e-6:
                set_a = 0
                return set_a

        if a == 0:
            if not in_goal:
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
