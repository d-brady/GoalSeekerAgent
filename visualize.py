import matplotlib.pyplot as plt
from simulation import BallSim
from agents.simple_reflex import SimpleReflexAgent
from agents.model_based_reflex import ModelBasedReflexAgent
from agents.llm_based_agent import LLMBasedAgent


sim = BallSim(x0=0, t_end=15, dt=0.01, noise_strength=0, seed=2, goal_center=10, goal_width=1, goal_movement='oscillating')

sim.set_acceleration(sim.max_acceleration)
while sim.step_counter_less_than_max_steps():
    # sim.step_with_agent(SimpleReflexAgent())
    # sim.step_with_agent(ModelBasedReflexAgent())
    sim.step_with_agent(LLMBasedAgent())


fig, ax = plt.subplots()
ax.plot(sim.t_arr, sim.x_arr)
ax.plot(sim.t_arr, sim.v_arr)
ax.plot(sim.t_arr, sim.a_arr)
ax.fill_between(x=sim.t_arr, y1=sim.goal_lower_arr, y2=sim.goal_upper_arr, color='r', alpha=0.5)
plt.show()

