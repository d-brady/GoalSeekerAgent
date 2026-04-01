import numpy as np


class BallSim:
    def __init__(self, x0: float, t_end: float, dt: float, noise_strength: float, seed: int, goal: tuple = (5, 6), max_acceleration: float = 5):

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

        self.v = 0
        self.a = 0
        self.max_acceleration = max_acceleration

        self.t_arr = np.linspace(0, self.t_end, self.max_steps + 1, endpoint=True)
        self.x_arr = np.full_like(self.t_arr, np.nan)
        self.v_arr = np.full_like(self.t_arr, np.nan)
        self.a_arr = np.full_like(self.t_arr, np.nan)

        self.x_arr[0] = self.x0
        self.v_arr[0] = self.v
        self.a_arr[0] = self.a


    def set_acceleration(self, new_a: float):

        if new_a > self.max_acceleration:
            self.a = self.max_acceleration
        elif new_a < -self.max_acceleration:
            self.a = -self.max_acceleration
        else:
            self.a = new_a


    def step(self):
        # leapfrog integrator in kick-drift-kick form

        self.v += 0.5 * self.a * self.dt  # half-step velocity update
        self.x += self.v * self.dt  # full-step position update
        self.v += 0.5 * self.a * self.dt  # half-step velocity update, assuming a is independent of x

        self.x += self.rng.normal(scale=self.noise_strength)  # add noise to position

        self.t += self.dt
        self.step_counter += 1

        self.x_arr[self.step_counter] = self.x
        self.v_arr[self.step_counter] = self.v
        self.a_arr[self.step_counter] = self.a


    def step_counter_less_than_max_steps(self):
        return self.step_counter < self.max_steps

    def in_goal(self):
        return self.goal[0] <= self.x <= self.goal[1]



