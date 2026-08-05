import pandas as pd
import numpy as np
import random

data = pd.read_excel("/Users/vinnu/Documents/Experiment_13_Q_Learning_Grid_Game_Dataset.xlsx")

states = len(data)
actions = 4

q_table = np.zeros((states, actions))

alpha = 0.1
gamma = 0.9
epsilon = 0.2

action_names = ["Up", "Down", "Left", "Right"]

for episode in range(100):

    state = 0

    while state < states - 1:

        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)
        else:
            action = np.argmax(q_table[state])

        reward = data.loc[state, "Reward"]

        next_state = state + 1

        q_table[state][action] = q_table[state][action] + alpha * (
            reward
            + gamma * np.max(q_table[next_state])
            - q_table[state][action]
        )

        state = next_state

print("Training Completed")
print()

print("Learned Policy")

for i in range(states):
    best_action = np.argmax(q_table[i])
    print("State", i, ":", action_names[best_action])

print()

print("Q Table")
print(q_table)
