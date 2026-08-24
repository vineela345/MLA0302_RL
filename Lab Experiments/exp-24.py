# 24) In an inventory management system, use Bellman's equation to find the optimal policy for ordering stock. Implement this in Python and demonstrate how the optimal policy minimizes costs.

max_inventory = int(input("Enter maximum inventory: "))
max_order = int(input("Enter maximum order quantity: "))
demand = int(input("Enter expected demand: "))

holding_cost = 2
order_cost = 3

V = [0] * (max_inventory + 1)
policy = [0] * (max_inventory + 1)

for inventory in range(max_inventory, -1, -1):

    best_cost = float("inf")
    best_order = 0

    for order in range(max_order + 1):

        new_inventory = min(
            inventory + order,
            max_inventory
        )

        ending_inventory = max(
            0,
            new_inventory - demand
        )

        cost = (
            order * order_cost
            + ending_inventory * holding_cost
        )

        total_cost = cost + V[ending_inventory]

        if total_cost < best_cost:
            best_cost = total_cost
            best_order = order

    V[inventory] = best_cost
    policy[inventory] = best_order

print("\n--- OUTPUT ---")

for inventory in range(max_inventory + 1):
    print(
        "Inventory:", inventory,
        "| Optimal Order:", policy[inventory],
        "| Minimum Cost:", V[inventory]
    )
