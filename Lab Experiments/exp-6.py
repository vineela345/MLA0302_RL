import random

ads = [0.2, 0.5, 0.8]
epsilon = 0.1

eg = 0
ucb = 0
ts = 0

for i in range(20):
    if random.random() < epsilon:
        ad = random.randint(0, 2)
    else:
        ad = ads.index(max(ads))
    if random.random() < ads[ad]:
        eg += 1

for i in range(20):
    ad = ads.index(max(ads))
    if random.random() < ads[ad]:
        ucb += 1

for i in range(20):
    ad = random.randint(0, 2)
    if random.random() < ads[ad]:
        ts += 1

print("Click Through Rate")
print("Epsilon-Greedy:", eg)
print("UCB:", ucb)
print("Thompson Sampling:", ts)
