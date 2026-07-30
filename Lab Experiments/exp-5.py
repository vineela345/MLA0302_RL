states = ["A", "B", "C"]

transitions = {
    "A": "B",
    "B": "C",
    "C": "C"
}

rewards = {
    "A": -1,
    "B": -1,
    "C": 10
}

gamma = 0.9

value = {"A": 0, "B": 0, "C": 0}

for i in range(5):
    new_value = {}
    for s in states:
        next_state = transitions[s]
        new_value[s] = rewards[next_state] + gamma * value[next_state]
    value = new_value

print("State Values:")
for s in states:
    print(s, "=", round(value[s], 2))

print("\nOptimal Policy:")
print("A -> Move to B")
print("B -> Move to C")
print("C -> Stay at C")
