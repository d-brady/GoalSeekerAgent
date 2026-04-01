import matplotlib.pyplot as plt
from simulation import BallSim

sim = BallSim(x0=0, t_end=10, dt=0.01, noise_strength=0, seed=2, goal=(-0.5, 0.5))

sim.set_acceleration(sim.max_acceleration)
while sim.step_counter_less_than_max_steps():

    if sim.step_counter % 10 == 0:
        sim.set_acceleration(-sim.a)

    sim.step()




fig, ax = plt.subplots()
ax.plot(sim.t_arr, sim.x_arr)
ax.plot(sim.t_arr, sim.v_arr)
ax.plot(sim.t_arr, sim.a_arr)
ax.vlines(x=sim.t_arr[-1], ymin=sim.goal[0], ymax=sim.goal[1], lw=3, color='r')
plt.show()

