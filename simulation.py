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
        self.t = 0.0
        self.step_counter = 0
        self.max_steps = int(np.ceil(self.t_end / self.dt))

        self.t_arr = np.linspace(0, self.t_end, self.max_steps + 1, endpoint=True)
        self.x_arr = np.full_like(self.t_arr, np.nan)
        self.x_arr[0] = self.x0


    def step(self, u: float):

        u_total = u + self.rng.normal(scale=self.noise_strength)
        self.x += self.dt * u_total
        self.t += self.dt

        self.step_counter += 1
        self.x_arr[self.step_counter] = self.x

    def step_counter_less_than_max_steps(self):
        return self.step_counter < self.max_steps

    def in_goal(self):
        return self.goal[0] <= self.x <= self.goal[1]



