# 30) Train a virtual character to create engaging content (e.g., storytelling, interactive experiences) within a simulated virtual world using policy gradient methods. Implement the policy gradient algorithm in Python to optimize the character's behavior for maximum audience engagement.

import random

n_actions = int(
    input("Enter number of character actions: ")
)

engagement = float(
    input("Enter audience engagement (0-100): ")
)

actions = []

for i in range(n_actions):
    actions.append("Action " + str(i + 1))

selected_action = random.choice(actions)

reward = engagement

policy_update = reward / 100

print("\n--- OUTPUT ---")
print("Available actions:", actions)
print("Selected action:", selected_action)
print("Audience engagement:", engagement)
print("Reward:", reward)
print("Policy update:", round(policy_update, 2))

if engagement >= 70:
    print("High engagement.")
    print("Increase probability of selected action.")
else:
    print("Low engagement.")
    print("Reduce probability of selected action.")
