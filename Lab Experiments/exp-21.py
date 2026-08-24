# 21) Use the Upper Confidence Bound (UCB) algorithm to dynamically select content for users on a streaming platform. Implement the UCB algorithm in Python and compare its effectiveness against other strategies.

import math
import random

n_contents = int(input("Enter number of contents: "))
n_rounds = int(input("Enter number of recommendations: "))

true_rewards = [random.uniform(0.2, 0.9) for _ in range(n_contents)]
counts = [0] * n_contents
rewards = [0] * n_contents
total_reward = 0

for i in range(n_contents):
    reward = 1 if random.random() < true_rewards[i] else 0
    counts[i] += 1
    rewards[i] += reward
    total_reward += reward

for t in range(n_contents, n_rounds):
    ucb_values = []

    for i in range(n_contents):
        average = rewards[i] / counts[i]
        confidence = math.sqrt(2 * math.log(t + 1) / counts[i])
        ucb_values.append(average + confidence)

    selected = ucb_values.index(max(ucb_values))
    reward = 1 if random.random() < true_rewards[selected] else 0

    counts[selected] += 1
    rewards[selected] += reward
    total_reward += reward

print("\n--- OUTPUT ---")
print("True rewards:", [round(x, 2) for x in true_rewards])
print("Content selections:", counts)
print("Total reward:", total_reward)
print("Average reward:", round(total_reward / n_rounds, 3))
print("Best content:", counts.index(max(counts)) + 1)
