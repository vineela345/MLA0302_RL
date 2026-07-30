gamma = 0.9

rewards = [0, 2, 5]

values = [0, 0, 0]

for i in range(10):
    for s in range(2):
        values[s] = rewards[s] + gamma * values[s + 1]

values[2] = rewards[2]

print("State Values")
for i in range(3):
    print("State", i, "=", round(values[i], 2))
