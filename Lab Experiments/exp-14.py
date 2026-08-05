import pandas as pd
import numpy as np

data = pd.read_excel("/Users/vinnu/Documents/Experiment_14_GridWorld_Policy_Iteration_Dataset.xlsx")

states = len(data)
actions = 4

gamma = 0.9

policy = np.zeros(states, dtype=int)
value = np.zeros(states)

while True:

    while True:

        delta = 0

        for s in range(states):

            if data.loc[s, "Goal"] == "Yes":
                continue

            reward = data.loc[s, "Reward"]

            next_state = min(s + 1, states - 1)

            old_value = value[s]

            value[s] = reward + gamma * value[next_state]

            delta = max(delta, abs(old_value - value[s]))

        if delta < 0.001:
            break

    stable = True

    for s in range(states):

        if data.loc[s, "Goal"] == "Yes":
            continue

        rewards = []

        for a in range(actions):

            next_state = min(s + 1, states - 1)

            rewards.append(data.loc[s, "Reward"] + gamma * value[next_state])

        best_action = np.argmax(rewards)

        if policy[s] != best_action:
            stable = False

        policy[s] = best_action

    if stable:
        break

action_names = ["Up", "Down", "Left", "Right"]

print("Optimal Policy")

for i in range(states):
    print("State", i, ":", action_names[policy[i]])

print()

print("State Values")

for i in range(states):
    print("State", i, ":", round(value[i], 2))
