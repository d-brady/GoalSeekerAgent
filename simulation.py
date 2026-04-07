import numpy as np


class BallSim:
    def __init__(self, x0: float, t_end: float, dt: float, noise_strength: float, seed: int, goal_center: float = 5.0,
                 goal_width: float = 1.0, max_acceleration: float = 5, goal_movement: str = None):

        self.x0 = x0
        self.t_end = t_end
        self.dt = dt

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

        self.initial_goal_center = goal_center
        self.initial_goal_width = goal_width

        supported_goal_movement_funcs = {
            'oscillating': self.gm_oscillation,
            'linear': self.gm_linear
        }


        if goal_movement is None:
            self.goal_center_arr = np.full_like(self.t_arr, self.initial_goal_center)
            self.goal_width_arr = np.full_like(self.t_arr, self.initial_goal_width)
        else:
            try:
                supported_goal_movement_funcs[goal_movement]()
            except KeyError as e:
                raise NotImplementedError(f'Goal Movement Function Not Supported: {e}')

        self.goal_lower_arr = self.goal_center_arr - self.goal_width_arr / 2
        self.goal_upper_arr = self.goal_center_arr + self.goal_width_arr / 2


    def gm_oscillation(self):
        self.goal_center_arr = 5 * np.sin(self.t_arr) + self.initial_goal_center
        self.goal_width_arr = np.full_like(self.t_arr, self.initial_goal_width)

    def gm_linear(self):
        self.goal_center_arr = self.initial_goal_center + self.t_arr
        self.goal_width_arr = np.full_like(self.t_arr, self.initial_goal_width)

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

    def step_with_agent(self, agent):

        state = self.get_state()
        self.a = agent.act(state)
        self.step()

    def get_state(self):

        if self.step_counter == 0:
            goal_center = [self.goal_center_arr[0]]
            goal_width = [self.goal_width_arr[0]]
        else:
            goal_center = self.goal_center_arr[:self.step_counter]
            goal_width = self.goal_width_arr[:self.step_counter]

        return {
            'x': self.x,
            'v': self.v,
            'a': self.a,
            'goal_center': goal_center,
            'goal_width': goal_width,
            'max_acceleration': self.max_acceleration
        }

    def step_counter_less_than_max_steps(self):
        return self.step_counter < self.max_steps

    def get_goal_bounds(self):
        return self.goal_lower_arr[self.step_counter] <= self.x <= self.goal_upper_arr[self.step_counter]
