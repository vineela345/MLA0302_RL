# 22) Simulate a k-armed bandit problem to optimize marketing campaign choices. Implement epsilon-greedy, UCB, and Thompson Sampling algorithms in Python and evaluate their performance.

import random
import math

k = int(input("Enter number of marketing campaigns: "))
rounds = int(input("Enter number of rounds: "))

probabilities = [random.uniform(0.2, 0.8) for _ in range(k)]

epsilon = 0.1
eg_counts = [0] * k
eg_rewards = [0] * k

for _ in range(rounds):
    if random.random() < epsilon:
        arm = random.randrange(k)
    else:
        averages = [
            eg_rewards[i] / eg_counts[i]
            if eg_counts[i] > 0 else 0
            for i in range(k)
        ]
        arm = averages.index(max(averages))

    reward = 1 if random.random() < probabilities[arm] else 0
    eg_counts[arm] += 1
    eg_rewards[arm] += reward

ucb_counts = [0] * k
ucb_rewards = [0] * k

for i in range(k):
    reward = 1 if random.random() < probabilities[i] else 0
    ucb_counts[i] += 1
    ucb_rewards[i] += reward

for t in range(k, rounds):
    values = []

    for i in range(k):
        average = ucb_rewards[i] / ucb_counts[i]
        confidence = math.sqrt(
            2 * math.log(t + 1) / ucb_counts[i]
        )
        values.append(average + confidence)

    arm = values.index(max(values))

    reward = 1 if random.random() < probabilities[arm] else 0
    ucb_counts[arm] += 1
    ucb_rewards[arm] += reward

success = [1] * k
failure = [1] * k

for _ in range(rounds):
    samples = [
        random.betavariate(success[i], failure[i])
        for i in range(k)
    ]

    arm = samples.index(max(samples))

    reward = 1 if random.random() < probabilities[arm] else 0

    if reward:
        success[arm] += 1
    else:
        failure[arm] += 1

print("\n--- OUTPUT ---")
print("Campaign probabilities:",
      [round(x, 2) for x in probabilities])
print("Epsilon-Greedy reward:", sum(eg_rewards))
print("UCB reward:", sum(ucb_rewards))
print("Thompson Sampling reward:", sum(success) - k)
