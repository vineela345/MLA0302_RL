import pandas as pd
import numpy as np
import random
import math

data = pd.read_excel("/Users/vinnu/Documents/Experiment_6_Advertisement_Bandit_Dataset.xlsx")

ads = data["Advertisement"].tolist()
prob = data["Click_Probability"].tolist()

n = len(ads)
rounds = 200

def reward(i):
    if random.random() < prob[i]:
        return 1
    return 0

epsilon = 0.1
count = [0] * n
value = [0] * n
eps = 0

for t in range(rounds):
    if random.random() < epsilon:
        arm = random.randint(0, n - 1)
    else:
        arm = np.argmax(value)

    r = reward(arm)
    count[arm] += 1
    value[arm] = ((value[arm] * (count[arm] - 1)) + r) / count[arm]
    eps += r

print("Epsilon Greedy CTR =", eps)

count = [0] * n
value = [0] * n
ucb = 0

for t in range(rounds):
    if 0 in count:
        arm = count.index(0)
    else:
        score = []
        for i in range(n):
            score.append(value[i] + math.sqrt((2 * math.log(t + 1)) / count[i]))
        arm = np.argmax(score)

    r = reward(arm)
    count[arm] += 1
    value[arm] = ((value[arm] * (count[arm] - 1)) + r) / count[arm]
    ucb += r

print("UCB CTR =", ucb)

success = [1] * n
failure = [1] * n
ts = 0

for t in range(rounds):
    sample = []

    for i in range(n):
        sample.append(np.random.beta(success[i], failure[i]))

    arm = np.argmax(sample)

    r = reward(arm)

    if r == 1:
        success[arm] += 1
    else:
        failure[arm] += 1

    ts += r

print("Thompson Sampling CTR =", ts)

result = {
    "Epsilon Greedy": eps,
    "UCB": ucb,
    "Thompson Sampling": ts
}

best = max(result, key=result.get)

print("Best Algorithm =", best)
