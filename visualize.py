import matplotlib.pyplot as plt
from simulation import BallSim
from agents.simple_reflex import SimpleReflexAgent
from agents.model_based_reflex import ModelBasedReflexAgent


sim = BallSim(x0=0, t_end=15, dt=0.01, noise_strength=0, seed=2, goal=(12, 13))

sim.set_acceleration(sim.max_acceleration)
while sim.step_counter_less_than_max_steps():
    # sim.step_with_agent(SimpleReflexAgent())
    sim.step_with_agent(ModelBasedReflexAgent())


fig, ax = plt.subplots()
ax.plot(sim.t_arr, sim.x_arr)
ax.plot(sim.t_arr, sim.v_arr)
ax.plot(sim.t_arr, sim.a_arr)
ax.vlines(x=sim.t_arr[-1], ymin=sim.goal[0], ymax=sim.goal[1], lw=3, color='r')
ax.fill_between(x=sim.t_arr, y1=sim.goal[0], y2=sim.goal[1], color='r', alpha=0.5)
plt.show()

