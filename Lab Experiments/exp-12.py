import pandas as pd
import numpy as np
import random

data = pd.read_excel("/Users/vinnu/Documents/Experiment_12_SARSA_Robot_Vacuum_Dataset.xlsx")

states = len(data)
actions = 3

q_table = np.zeros((states, actions))

alpha = 0.1
gamma = 0.9
epsilon = 0.2

action_names = ["Clean", "Move", "Recharge"]

for episode in range(100):

    state = 0

    if random.uniform(0, 1) < epsilon:
        action = random.randint(0, actions - 1)
    else:
        action = np.argmax(q_table[state])

    while state < states - 1:

        reward = data.loc[state, "Reward"]

        if action == 0:
            reward = reward + 2

        elif action == 1:
            reward = reward - data.loc[state, "Battery_Cost"]

        else:
            reward = -1

        next_state = state + 1

        if random.uniform(0, 1) < epsilon:
            next_action = random.randint(0, actions - 1)
        else:
            next_action = np.argmax(q_table[next_state])

        q_table[state][action] = q_table[state][action] + alpha * (
            reward
            + gamma * q_table[next_state][next_action]
            - q_table[state][action]
        )

        state = next_state
        action = next_action

print("Training Completed")
print()

print("Optimal Policy")

for i in range(states):
    best_action = np.argmax(q_table[i])
    print("Room", i + 1, ":", action_names[best_action])

print()

print("Q Table")
print(q_table)
