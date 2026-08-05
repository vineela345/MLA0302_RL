import pandas as pd

data = pd.read_excel("/Users/vinnu/Documents/Experiment_7_Warehouse_Bellman_Dataset.xlsx")

states = data["State"].tolist()
rewards = data["Reward"].tolist()

gamma = 0.9

values = [0] * len(states)

for k in range(10):
    new_values = []

    for i in range(len(states)):
        value = rewards[i] + gamma * values[i]
        new_values.append(value)

    values = new_values

print("State Values")

for i in range(len(states)):
    print("State", states[i], "=", round(values[i], 2))

best = values.index(max(values))

print("\nBest Delivery Point =", states[best])
