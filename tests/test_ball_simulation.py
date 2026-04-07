from simulation import BallSim
import numpy as np


def test_initial_state():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=0, seed=42)

    assert(sim.x == 0)
    assert(sim.t == 0)


def test_final_state():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=0, seed=42)

    while sim.step_counter_less_than_max_steps():
        sim.step()

    assert(sim.x == 0)
    assert(np.isclose(sim.t, sim.t_end))


def test_filling_of_save_arrays():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=1, seed=42)

    while sim.step_counter_less_than_max_steps():
        sim.step()

    assert sim.max_steps + 1 == len(sim.x_arr)
    assert not np.isnan(sim.x_arr).any()
    assert not np.isnan(sim.v_arr).any()
    assert not np.isnan(sim.a_arr).any()


def test_method_in_goal():

    sim = BallSim(x0=0, t_end=1, dt=0.1, noise_strength=0, seed=42, goal=(-0.1, 0.1))

    while sim.step_counter_less_than_max_steps():
        sim.step()

    assert sim.in_goal()


def test_equations_of_motion():

    sim = BallSim(x0=0, t_end=5, dt=0.1, noise_strength=0, seed=42, goal=(-0.1, 0.1))

    assert(sim.max_acceleration > 0)
    assert(sim.v == 0)
    assert(sim.x == 0)

    sim.set_acceleration(new_a=sim.max_acceleration)

    while sim.step_counter_less_than_max_steps():
        sim.step()

    assert sim.a == sim.max_acceleration
    assert np.isclose(sim.v, sim.max_acceleration * sim.t_end)
    assert np.isclose(sim.x, 0.5 * sim.max_acceleration * sim.t_end ** 2)
