import pandas as pd
import numpy as np
import random

data = pd.read_excel("/Users/vinnu/Documents/Experiment_11_Double_DQN_Stock_Trading_Dataset.xlsx")

prices = data["Close"].tolist()

q_table = np.zeros((len(prices), 3))

alpha = 0.1
gamma = 0.9
epsilon = 0.2

cash = 10000
stock = 0

for episode in range(100):

    cash = 10000
    stock = 0

    for state in range(len(prices) - 1):

        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 2)
        else:
            action = np.argmax(q_table[state])

        reward = 0

        if action == 0:
            if cash >= prices[state]:
                cash -= prices[state]
                stock += 1

        elif action == 1:
            if stock > 0:
                cash += prices[state]
                stock -= 1
                reward = prices[state] - prices[max(state - 1, 0)]

        else:
            reward = -1

        next_state = state + 1

        q_table[state][action] = q_table[state][action] + alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state][action]
        )

final_profit = cash + stock * prices[-1] - 10000

print("Final Cash:", cash)
print("Stocks Held:", stock)
print("Final Profit:", final_profit)
print("\nQ Table")
print(q_table)
