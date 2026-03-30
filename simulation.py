import numpy as np


class BallSim:
    def __init__(self, x0: float, t_end: float, dt: float, noise_strength: float, seed: int, goal: tuple = (5, 6)):

        self.x0 = x0
        self.t_end = t_end
        self.dt = dt
        self.goal = goal

        self.rng = np.random.default_rng(seed)
        self.noise_strength = noise_strength

        self.x = self.x0
        self.t = 0.

        self.t_arr = np.arange(0, self.t_end, self.dt)
        self.x_arr = np.full_like(self.t_arr, np.nan)


    def step(self, u: float):

        u_total = u + self.rng.normal(scale=self.noise_strength)
        self.x += self.dt * u_total
        self.t += self.dt

        # Save current state
        idx = int(self.t / self.dt) - 1  # match array index
        if idx < len(self.x_arr):
            self.x_arr[idx] = self.x

    def in_goal(self):
        return self.goal[0] <= self.x <= self.goal[1]



