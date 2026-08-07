import pandas as pd
import numpy as np

data = pd.read_excel("/Users/vinnu/Documents/Experiment_20_Epsilon_Greedy_Content_Dataset.xlsx")

print("Dataset Loaded Successfully")
print(data.head())

contents = data.iloc[:, 1].unique()

n = len(contents)

Q = np.zeros(n)
N = np.zeros(n)

epsilon = 0.2
rounds = 500

for i in range(rounds):

    if np.random.rand() < epsilon:
        action = np.random.randint(n)
    else:
        action = np.argmax(Q)

    reward = np.random.randint(0, 2)

    N[action] += 1
    Q[action] = Q[action] + (reward - Q[action]) / N[action]

print("\nAverage Reward of Each Content")

for i in range(n):
    print(contents[i], ":", round(Q[i], 3))

best = np.argmax(Q)

print("\nBest Recommended Content:", contents[best])

print("\nTraining Completed")
