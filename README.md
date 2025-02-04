# Green Light Is All You Need

## A Deep Reinforcement Learning Approach for Traffic Light Management

![](https://https://github.com/ArielPom/GreenLightIsAllYouNeed/assets/greenlight_gif.gif)

### Authors
<p align="center">
  <strong>Ariel Pomeranchik | Oren Goldberg</strong>
</p>

## Dependencies and Versions

The repo is based on a jupyter notebook, which handles the installation of the required packages.
The following packages and versions were used in the project:

| Package  | Version |
|----------|---------|
| Python   | 3.10.12   |
| PyTorch  | 2.5.1   |
| NumPy    | 2.2.2   |
| SciPy    | 1.15.1   |
| SUMO     | 1.21.0  |

## Motivation
Traffic congestion is a major issue in urban areas, leading to increased travel times, fuel consumption, and pollution. Traditional traffic light control systems rely on fixed-time or rule-based approaches that fail to adapt to real-time traffic conditions.

In this project, we propose a Deep Reinforcement Learning (DRL) approach to optimize traffic light management, reducing congestion and improving traffic flow dynamically.

## Deep Reinforcement Learning Approach
We employ **Proximal Policy Optimization (PPO)**, a popular reinforcement learning algorithm, to train an intelligent agent that learns optimal traffic light control policies. PPO is an on-policy algorithm that balances exploration and exploitation efficiently while maintaining stability in training. 




## SUMO & TraCI
This project relies on **SUMO (Simulation of Urban MObility)** for traffic simulation and **TraCI (Traffic Control Interface)** to interact with the simulation environment in real time. 

- **SUMO** simulates realistic vehicle behavior, road networks, and traffic light interactions.
- **TraCI** allows Python-based control over SUMO, enabling reinforcement learning agents to modify traffic signals dynamically and collect traffic statistics during simulations.

for changing the simulation, changes should be made to the files inculed in the **/sumo_files** directory

## Running the Simulation
The project can be run in two modes:

1. **GUI Mode** – Runs SUMO with a graphical interface to visualize traffic flow.
2. **Headless Mode** – Runs SUMO without a graphical interface for faster simulations.

this modes are defined by the configuraion of **SUMO_APP** variable in the notebook
```python
# simulation command
SUMO_HEADLESS = "sumo"
SUMO_GUI = "sumo-gui"
SUMO_APP = SUMO_HEADLESS
```

also, the global variable **EPISODES_GUI** can be changed, to set the number of episodes to run in GUI mode. for example when set to 5 , every 5th episode will be run in GUI mode



## References
We built upon ideas from existing research in DRL-based traffic signal control, particularly the following projects:

- [Deep Q-Learning Agent for Traffic Signal Control](https://github.com/AndreaVidali/Deep-QLearning-Agent-for-Traffic-Signal-Control/tree/master/TLCS)
- [StageLight: Multi-Agent Traffic Signal Control](https://github.com/GangSuUGA/StageLight?tab=readme-ov-file)

---
This README provides an overview of our project, its motivation, implementation details, and references to related work. For more details, check out the code and experiments in our repository!