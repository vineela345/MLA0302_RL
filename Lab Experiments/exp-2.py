grid = [
    [0, 0, 2],
    [0, -2, 0],
    [0, 0, 5]
]

value = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

gamma = 0.9

for k in range(10):
    for i in range(3):
        for j in range(3):

            reward = grid[i][j]

            if i < 2:
                next_value = value[i + 1][j]
            else:
                next_value = value[i][j]

            value[i][j] = reward + gamma * next_value

print("Value Function")

for row in value:
    print(row)
