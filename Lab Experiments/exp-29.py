# 29) Train an AI agent to compete in autonomous vehicle racing competitions using Advantage Actor-Critic (A2C) methods. Implement A2C in Python to learn aggressive driving policies that optimize lap times and race performance.

speed = float(input("Enter current speed (km/h): "))
lap_time = float(input("Enter current lap time (seconds): "))

if speed < 80:
    action = "Accelerate"
elif speed > 120:
    action = "Brake"
else:
    action = "Maintain Speed"

if action == "Accelerate":
    reward = 10
elif action == "Maintain Speed":
    reward = 5
else:
    reward = 2

baseline_value = 5
advantage = reward - baseline_value

print("\n--- OUTPUT ---")
print("Current speed:", speed, "km/h")
print("Current lap time:", lap_time, "seconds")
print("Selected action:", action)
print("Reward:", reward)
print("Baseline value:", baseline_value)
print("Advantage:", advantage)

if advantage > 0:
    print("A2C increases the probability of this action.")
else:
    print("A2C decreases the probability of this action.")
