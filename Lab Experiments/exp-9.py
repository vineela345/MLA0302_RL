import pandas as pd
import random

data = pd.read_excel("/Users/vinnu/Documents/Experiment_9_Call_Center_MonteCarlo_Dataset.xlsx")

rewards = data["Reward"].tolist()
reps = data["Representative"].tolist()

returns = []

for i in range(len(rewards)):
    total = 0

    for j in range(100):
        total += rewards[i] + random.randint(-2, 2)

    returns.append(total / 100)

print("Estimated Value Function")

for i in range(len(reps)):
    print(reps[i], "=", round(returns[i], 2))

best = returns.index(max(returns))

print("\nBest Representative =", reps[best])
