import random

policy = 0.5

for i in range(10):

    reward = random.randint(-2, 5)

    policy = policy + 0.1 * reward

    print("Step", i + 1, "Reward =", reward, "Policy =", round(policy, 2))

print("\nFinal Policy =", round(policy, 2))
