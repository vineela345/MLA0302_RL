# 23) Explain the relationship between policy and value functions using a practical gridworld example. Implement this relationship in Python and visualize how different policies affect the value function.

grid_size = int(input("Enter grid size: "))

goal = (grid_size - 1, grid_size - 1)

policy = {}
value = {}

for r in range(grid_size):
    for c in range(grid_size):
        if (r, c) == goal:
            policy[(r, c)] = "G"
        elif r < grid_size - 1:
            policy[(r, c)] = "D"
        else:
            policy[(r, c)] = "R"

for r in range(grid_size):
    for c in range(grid_size):
        distance = abs(goal[0] - r) + abs(goal[1] - c)
        value[(r, c)] = -distance

print("\n--- POLICY ---")

for r in range(grid_size):
    for c in range(grid_size):
        print(policy[(r, c)], end=" ")
    print()

print("\n--- VALUE FUNCTION ---")

for r in range(grid_size):
    for c in range(grid_size):
        print(f"{value[(r,c)]:3}", end=" ")
    print()

print("\nG = Goal")
print("D = Down")
print("R = Right")
