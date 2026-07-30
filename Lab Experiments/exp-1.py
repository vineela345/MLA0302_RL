import random

grid = [
    [0, 0, 1, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 1, -1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, -1, 0, 1]
]

row = 0
col = 0
reward = 0

moves = ["UP", "DOWN", "LEFT", "RIGHT"]

print("Robot Navigation\n")

for i in range(15):

    move = random.choice(moves)

    if move == "UP" and row > 0:
        row -= 1
    elif move == "DOWN" and row < 4:
        row += 1
    elif move == "LEFT" and col > 0:
        col -= 1
    elif move == "RIGHT" and col < 4:
        col += 1

    if grid[row][col] == 1:
        print("Step", i + 1, ":", move, "-> Dirt Found (+1)")
        reward += 1
        grid[row][col] = 0

    elif grid[row][col] == -1:
        print("Step", i + 1, ":", move, "-> Obstacle (-1)")
        reward -= 1

    else:
        print("Step", i + 1, ":", move, "-> Empty Cell")

print("\nTotal Reward =", reward)
