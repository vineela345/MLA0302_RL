import pandas as pd
import numpy as np

data = pd.read_excel("/Users/vinnu/Documents/Experiment_19_Customer_Churn_MC_Dataset.xlsx")
print("Dataset Loaded Successfully")
print(data.head())

returns = []
state_values = []

episodes = 100

for episode in range(episodes):

    episode_rewards = []

    for index, row in data.iterrows():

        if row["Churn"] == 1:
            reward = -1
        else:
            reward = 1

        episode_rewards.append(reward)

    G = 0

    for reward in reversed(episode_rewards):
        G = reward + 0.9 * G

    returns.append(G)

average_return = np.mean(returns)

print("\nMonte Carlo Policy Evaluation")
print("Average Return:", average_return)

if average_return > 0:
    print("Policy Prediction: Most customers stay subscribed")
else:
    print("Policy Prediction: High customer churn")

print("\nTraining Completed")
