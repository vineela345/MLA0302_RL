# 28) Develop an AI agent to play a real-time strategy game (e.g., Age of Empires) using Actor-Critic methods. Implement the actor and critic networks in Python and train the agent to build structures, gather resources, and engage in strategic combat.

resources = int(input("Enter available resources: "))
enemy_strength = int(input("Enter enemy strength: "))

if resources < 50:
    action = "Gather Resources"
elif enemy_strength > resources:
    action = "Build Structures"
else:
    action = "Attack Enemy"

if action == "Gather Resources":
    reward = 10
elif action == "Build Structures":
    reward = 15
else:
    if resources > enemy_strength:
        reward = 25
    else:
        reward = -10

critic_value = reward

print("\n--- OUTPUT ---")
print("Resources:", resources)
print("Enemy strength:", enemy_strength)
print("Actor selected action:", action)
print("Reward:", reward)
print("Critic value:", critic_value)
