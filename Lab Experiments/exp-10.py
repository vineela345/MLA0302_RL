import pandas as pd

data = pd.read_excel("/Users/vinnu/Documents/Experiment_10_Policy_Gradient_Investment_Dataset.xlsx")

actions = data["Action"].tolist()
returns = data["Portfolio_Return"].tolist()

policy = 0

for i in range(len(returns)):
    policy = policy + 0.1 * returns[i]

print("Updated Policy Value =", round(policy, 4))

print("\nInvestment Returns")

for i in range(len(actions)):
    print(actions[i], "=", returns[i])

best = returns.index(max(returns))

print("\nBest Action =", actions[best])
