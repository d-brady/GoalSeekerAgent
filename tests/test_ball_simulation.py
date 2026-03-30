from simulation import BallSim
import numpy as np


def test_initial_state():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=0, seed=42)

    assert(sim.x == 0)
    assert(sim.t == 0)


def test_time_evolution_no_kicks():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=0, seed=42)

    while sim.step_counter_less_than_max_steps():
        sim.step(u=0)

    assert(sim.x == 0)
    assert(np.isclose(sim.t, sim.t_end))


def test_time_evolution_all_array_values_filled_and_real():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=1, seed=42)

    while sim.step_counter_less_than_max_steps():
        sim.step(u=0)

    assert sim.max_steps + 1 == len(sim.x_arr)
    assert not np.isnan(sim.x_arr).any()


def test_ball_in_goal():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=0, seed=42, goal=(-0.1, 0.1))

    while sim.step_counter_less_than_max_steps():
        sim.step(u=0)

    assert sim.in_goal()