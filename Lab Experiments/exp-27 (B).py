# 27) Implement a robot that navigates a maze to reach the exit, with rewards for reaching the exit and penalties for hitting walls, and use REINFORCE to find the optimal navigation policy.

rows = int(input("Enter number of maze rows: "))
cols = int(input("Enter number of maze columns: "))

position = (0, 0)
goal = (rows - 1, cols - 1)

steps = 0
reward = 0

while position != goal:

    row, col = position

    if col < cols - 1:
        position = (row, col + 1)

    elif row < rows - 1:
        position = (row + 1, col)

    steps += 1
    reward -= 1

    if steps >= 100:
        break

if position == goal:
    reward += 100

print("\n--- OUTPUT ---")
print("Start:", (0, 0))
print("Goal:", goal)
print("Final position:", position)
print("Steps:", steps)
print("Total reward:", reward)

if position == goal:
    print("Robot successfully reached the exit.")
else:
    print("Robot failed to reach the exit.")
