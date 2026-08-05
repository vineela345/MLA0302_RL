import pandas as pd
import numpy as np

data = pd.read_excel("/Users/vinnu/Documents/Experiment_16_Bellman_Robot_Navigation_Dataset.xlsx")

states = len(data)
gamma = 0.9

value = np.zeros(states)

while True:

    delta = 0

    for s in range(states):

        reward = data.loc[s, "Reward"]

        if data.loc[s, "Goal"] == "Yes":
            continue

        next_state = min(s + 1, states - 1)

        old_value = value[s]

        value[s] = reward + gamma * value[next_state]

        delta = max(delta, abs(old_value - value[s]))

    if delta < 0.001:
        break

print("Optimal State Values")
print()

for i in range(states):
    print("State", i, ":", round(value[i], 2))

print()

print("Optimal Path")

path = []

current = 0

while current < states - 1:
    path.append(current)
    current += 1

path.append(states - 1)

print(path)
