from agents.base import BaseAgent
import numpy as np


class SimpleReflexAgent(BaseAgent):

    def __init__(self):
        super().__init__()

        # Reflex based on PID Control
        self.k_p = 1.0  # proportional term, depends on distance
        self.k_d = 0.5  # derivative term, depends on velocity


    def act(self, state):

        x = state['x']
        v = state['v']
        a = state['a']
        goal_center = state['goal_center'][-1]  # take only current center
        goal_width = state['goal_width'][-1]

        in_goal = (goal_center - goal_width / 2 <= x <= goal_center + goal_width / 2)

        if in_goal:
            if np.abs(v) < 1e-6:
                set_a = 0
            else:
                set_a = -v
        else:
            set_a = self.k_p * (goal_center - x) - self.k_d * v

        return set_a





