import pandas as pd
import numpy as np

data = pd.read_excel("/Users/vinnu/Documents/Experiment_18_Manufacturing_RL_Dataset.xlsx")
print("Dataset Loaded Successfully")
print(data.head())

states = ["Low", "Medium", "High"]
actions = ["Decrease", "Maintain", "Increase"]

num_states = len(states)
num_actions = len(actions)

Q = np.zeros((num_states, num_actions))

alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 500

for episode in range(episodes):

    state = np.random.randint(num_states)

    if np.random.rand() < epsilon:
        action = np.random.randint(num_actions)
    else:
        action = np.argmax(Q[state])

    reward = np.random.randint(70, 101)

    next_state = np.random.randint(num_states)

    Q[state][action] = Q[state][action] + alpha * (
        reward + gamma * np.max(Q[next_state]) - Q[state][action]
    )
    
print("\nQ Table")
print(Q)

print("\nOptimal Policy")

for i in range(num_states):
    print(states[i], "->", actions[np.argmax(Q[i])])

print("\nTraining Completed")
