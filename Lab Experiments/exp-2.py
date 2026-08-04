import pandas as pd

file_path = "/Users/vinnu/Documents/Warehouse_RL_Dataset.xlsx"

states = pd.read_excel(file_path, sheet_name="Warehouse_States")
policy = pd.read_excel(file_path, sheet_name="Policy")
transitions = pd.read_excel(file_path, sheet_name="Transitions")

gamma = 0.9

V = {}

for state in states["State_ID"]:
    V[state] = 0

reward = {}
for i in range(len(states)):
    reward[states["State_ID"][i]] = states["Reward"][i]

for _ in range(20):
    new_V = V.copy()

    for i in range(len(policy)):
        state = policy["State"][i]
        action = policy["Action"][i]

        trans = transitions[
            (transitions["Current_State"] == state) &
            (transitions["Action"] == action)
        ]

        if len(trans) > 0:
            next_state = trans.iloc[0]["Next_State"]
            prob = trans.iloc[0]["Probability"]

            new_V[state] = prob * (reward[next_state] + gamma * V[next_state])

    V = new_V

print("State Value Function")

for state in V:
    print(state, "=", round(V[state], 2))
