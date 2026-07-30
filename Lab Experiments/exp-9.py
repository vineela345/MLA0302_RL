import random

policies = ["Policy A", "Policy B"]

for policy in policies:

    total_reward = 0

    for i in range(20):
        reward = random.randint(1, 5)
        total_reward += reward

    average = total_reward / 20

    print(policy)
    print("Average Value =", average)
    print()
