# 27) Implement an agent that manages a financial portfolio, choosing stocks to maximize returns and minimize risk using an Actor-Critic (A3C) method to optimize investment.

import random

n_stocks = int(input("Enter number of stocks: "))
investment = float(input("Enter investment amount: "))

returns = [
    random.uniform(-0.05, 0.10)
    for _ in range(n_stocks)
]

selected_stock = returns.index(
    max(returns)
)

profit = investment * returns[selected_stock]

critic_value = profit

print("\n--- OUTPUT ---")
print(
    "Expected stock returns:",
    [round(x, 3) for x in returns]
)
print("Selected stock:", selected_stock + 1)
print("Investment:", investment)
print("Profit/Loss:", round(profit, 2))
print("Critic value:", round(critic_value, 2))

if profit >= 0:
    print("Decision: GOOD INVESTMENT")
else:
    print("Decision: HIGH RISK")
