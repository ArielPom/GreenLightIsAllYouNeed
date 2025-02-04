# Green Light Is All You Need

## A Deep Reinforcement Learning Approach for Traffic Light Management

![image](https://github.com/user-attachments/assets/abe94a81-7612-4b8c-9868-f6f10d65e69a)

![image](https://github.com/user-attachments/assets/77cd9d5b-75c4-4420-932f-4c4a5f7e55ec)

### Authors
<p align="center">
  <strong>Ariel Pomeranchik & Oren Goldberg</strong>
</p>

## Motivation
Traffic congestion is a major issue in urban areas, leading to increased travel times, fuel consumption, and pollution. Traditional traffic light control systems rely on fixed-time or rule-based approaches that fail to adapt to real-time traffic conditions.

In this project, we propose a Deep Reinforcement Learning (DRL) approach to optimize traffic light management, reducing congestion and improving traffic flow dynamically.

## Deep Reinforcement Learning Approach
We employ **Proximal Policy Optimization (PPO)**, a popular reinforcement learning algorithm, to train an intelligent agent that learns optimal traffic light control policies. PPO is an on-policy algorithm that balances exploration and exploitation efficiently while maintaining stability in training. 

PPO incorporates **entropy loss** to encourage policy exploration by preventing premature convergence to suboptimal strategies. Additionally, **random action selection** is used during training to enhance policy robustness, allowing the agent to experience diverse traffic patterns before converging to an optimal policy.

## Requirements
To run this project, you need the following Python packages:

```bash
pip install torch gymnasium stable-baselines3 sumo-tools traci numpy matplotlib
```

### SUMO & TraCI
This project relies on **SUMO (Simulation of Urban MObility)** for traffic simulation and **TraCI (Traffic Control Interface)** to interact with the simulation environment in real time. 

- **SUMO** simulates realistic vehicle behavior, road networks, and traffic light interactions.
- **TraCI** allows Python-based control over SUMO, enabling reinforcement learning agents to modify traffic signals dynamically and collect traffic statistics during simulations.

Ensure that SUMO is installed and accessible from your environment before running the simulations.

## Running the Simulation
The project can be run in two modes:

1. **GUI Mode** – Runs SUMO with a graphical interface to visualize traffic flow.
2. **Headless Mode** – Runs SUMO without a graphical interface for faster simulations.

To start training:
```bash
python train.py --mode gui   # Runs with visualization
python train.py --mode headless  # Runs without GUI
```

## References
We built upon ideas from existing research in DRL-based traffic signal control, particularly the following projects:

- [Deep Q-Learning Agent for Traffic Signal Control](https://github.com/AndreaVidali/Deep-QLearning-Agent-for-Traffic-Signal-Control/tree/master/TLCS)
- [StageLight: Multi-Agent Traffic Signal Control](https://github.com/GangSuUGA/StageLight?tab=readme-ov-file)

---
This README provides an overview of our project, its motivation, implementation details, and references to related work. For more details, check out the code and experiments in our repository!
