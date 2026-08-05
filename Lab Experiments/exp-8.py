import pandas as pd

data = pd.read_excel("/Users/vinnu/Documents/Experiment_8_Autonomous_Car_Policy_Dataset.xlsx")

places = data["Intersection"].tolist()
rewards = data["Reward"].tolist()

gamma = 0.9

values = [0] * len(places)

for k in range(10):
    new_values = []

    for i in range(len(places)):
        value = rewards[i] + gamma * values[i]
        new_values.append(value)

    values = new_values

print("Policy Values")

for i in range(len(places)):
    print(places[i], "=", round(values[i], 2))

best = values.index(max(values))

print("\nBest Destination =", places[best])
