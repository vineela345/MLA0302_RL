# 25) Model a smart grid that manages energy consumption and production to minimize costs and balance supply and demand using Trust Region Policy Optimization (TRPO) to optimize energy management.

import numpy as np

demand = float(input("Enter energy demand (kWh): "))
production = float(input("Enter renewable energy production (kWh): "))
price = float(input("Enter electricity price per kWh: "))

policy = 0.5

available_energy = production * policy

grid_energy = max(
    0,
    demand - available_energy
)

cost = grid_energy * price

if cost > 0:
    policy += 0.05
else:
    policy -= 0.02

policy = np.clip(policy, 0, 1)

print("\n--- OUTPUT ---")
print("Energy demand:", demand, "kWh")
print("Renewable production:", production, "kWh")
print("Electricity price:", price)
print("Initial policy: 0.50")
print("Updated policy:", round(policy, 2))
print("Grid energy required:", round(grid_energy, 2), "kWh")
print("Energy cost:", round(cost, 2))
