import pandas as pd
import numpy as np
import random

data = pd.read_excel("/Users/vinnu/Documents/Experiment_15_Monte_Carlo_Call_Center_Dataset.xlsx")

states = len(data)
actions = 3

action_names = ["Assign Rep_A", "Assign Rep_B", "Assign Rep_C"]

q_table = np.zeros((states, actions))
returns = [[[] for _ in range(actions)] for _ in range(states)]

gamma = 0.9
epsilon = 0.2

for episode in range(500):

    episode_memory = []

    for state in range(states):

        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)
        else:
            action = np.argmax(q_table[state])

        estimated = data.loc[state, "Estimated_Time"]
        actual = data.loc[state, "Actual_Time"]
        satisfaction = data.loc[state, "Customer_Satisfaction"]

        reward = satisfaction * 10 - abs(actual - estimated)

        episode_memory.append((state, action, reward))

    G = 0

    visited = set()

    for state, action, reward in reversed(episode_memory):

        G = gamma * G + reward

        if (state, action) not in visited:

            visited.add((state, action))

            returns[state][action].append(G)

            q_table[state][action] = np.mean(returns[state][action])

print("Training Completed")
print()

print("Optimal Assignment Policy")

for i in range(states):
    best_action = np.argmax(q_table[i])
    print("Call", i + 1, ":", action_names[best_action])

print()

print("Q Table")
print(np.round(q_table, 2))
