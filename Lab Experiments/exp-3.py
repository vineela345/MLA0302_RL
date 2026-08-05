import pandas as pd
import numpy as np
import random
import math

data = pd.read_excel("/Users/vinnu/Documents/Experiment_3_Dynamic_Pricing_Bandit_Dataset(1).xlsx")

prices = data["Price ($)"].tolist()
prob = data["Expected_Conversion_Rate"].tolist()

n = len(prices)
rounds = 200

def reward(i):
    if random.random() < prob[i]:
        return prices[i]
    return 0

epsilon = 0.1
count = [0] * n
value = [0] * n
eps_total = 0

for t in range(rounds):
    if random.random() < epsilon:
        arm = random.randint(0, n - 1)
    else:
        arm = np.argmax(value)

    r = reward(arm)
    count[arm] += 1
    value[arm] = ((value[arm] * (count[arm] - 1)) + r) / count[arm]
    eps_total += r

print("Epsilon Greedy Revenue =", eps_total)

count = [0] * n
value = [0] * n
ucb_total = 0

for t in range(rounds):
    if 0 in count:
        arm = count.index(0)
    else:
        ucb = []
        for i in range(n):
            score = value[i] + math.sqrt((2 * math.log(t + 1)) / count[i])
            ucb.append(score)
        arm = np.argmax(ucb)

    r = reward(arm)
    count[arm] += 1
    value[arm] = ((value[arm] * (count[arm] - 1)) + r) / count[arm]
    ucb_total += r

print("UCB Revenue =", ucb_total)

success = [1] * n
failure = [1] * n
ts_total = 0

for t in range(rounds):
    sample = []

    for i in range(n):
        sample.append(np.random.beta(success[i], failure[i]))

    arm = np.argmax(sample)

    r = reward(arm)

    if r > 0:
        success[arm] += 1
    else:
        failure[arm] += 1

    ts_total += r

print("Thompson Sampling Revenue =", ts_total)

revenues = {
    "Epsilon Greedy": eps_total,
    "UCB": ucb_total,
    "Thompson Sampling": ts_total
}

best = max(revenues, key=revenues.get)

print("Best Strategy =", best)
