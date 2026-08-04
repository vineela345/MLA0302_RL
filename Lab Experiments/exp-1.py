import pandas as pd

data = pd.read_excel(r"/Users/vinnu/Downloads/exp01_dataset.xlsx")

reward = 0

print("AUTONOMOUS CLEANING ROBOT")
print("-" * 30)

for index, row in data.iterrows():

    r = int(row["Row"])
    c = int(row["Col"])

    print(f"\nRobot Position : ({r},{c})")

    if row["Obstacle"] == 1:
        print("Obstacle Found")
        reward -= 1

    elif row["Dirt"] == 1:
        print("Dirt Cleaned")
        reward += 1

    else:
        print("Empty Cell")

print("\n" + "-" * 30)
print("Final Reward =", reward)

if reward > 0:
    print("Optimal Policy Achieved")
else:
    print("Policy Needs Improvement")
