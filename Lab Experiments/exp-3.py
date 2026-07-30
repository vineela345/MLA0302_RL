import random

rewards = [4, 7, 10]
epsilon = 0.1

eg = 0
ucb = 0
ts = 0

for i in range(20):
    if random.random() < epsilon:
        a = random.randint(0, 2)
    else:
        a = rewards.index(max(rewards))
    eg += rewards[a]

for i in range(20):
    a = rewards.index(max(rewards))
    ucb += rewards[a]

for i in range(20):
    a = random.randint(0, 2)
    ts += rewards[a]

print("Epsilon-Greedy Revenue:", eg)
print("UCB Revenue:", ucb)
print("Thompson Sampling Revenue:", ts)
