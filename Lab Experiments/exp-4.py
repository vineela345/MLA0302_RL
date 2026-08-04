import pandas as pd
import numpy as np

data = pd.read_excel("/Users/vinnu/Documents/Experiment_4_Drone_Policy_Iteration_Dataset.xlsx")

reward = data["Reward"].values.reshape(5,5)

gamma = 0.9
value = np.zeros((5,5))
policy = np.zeros((5,5), dtype=int)

actions = [(-1,0),(1,0),(0,-1),(0,1)]

for k in range(10):

    for i in range(5):
        for j in range(5):

            a = policy[i][j]

            x = max(0, min(4, i + actions[a][0]))
            y = max(0, min(4, j + actions[a][1]))

            value[i][j] = reward[x][y] + gamma * value[x][y]

    for i in range(5):
        for j in range(5):

            best = -999
            best_action = 0

            for a in range(4):

                x = max(0, min(4, i + actions[a][0]))
                y = max(0, min(4, j + actions[a][1]))

                v = reward[x][y] + gamma * value[x][y]

                if v > best:
                    best = v
                    best_action = a

            policy[i][j] = best_action

print("Optimal Policy")
print(policy)

print("\nState Values")
print(value)
