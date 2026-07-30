grid = [
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
]

value = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

policy = [
    ["R", "R", "D"],
    ["D", "X", "D"],
    ["R", "R", "G"]
]

gamma = 0.9

for k in range(5):
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            if grid[i][j] == -1:
                continue
            if grid[i][j] == 1:
                value[i][j] = 5
            elif j < 2:
                value[i][j] = grid[i][j] + gamma * value[i][j + 1]
            elif i < 2:
                value[i][j] = grid[i][j] + gamma * value[i + 1][j]

print("Value Function")
for row in value:
    print(row)

print("\nPolicy")
for row in policy:
    print(row)
