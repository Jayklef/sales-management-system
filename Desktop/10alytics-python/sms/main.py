"""FreshMart automated sales management system.

This program records transactions for three pre-registered cashiers
and generates an end-of-day sales report.
"""


# Pre-registered cashier names
cashier_names: list[str] = ["Sarah", "David", "Grace"]

# Each position matches the corresponding cashier in cashier_names
transaction_counts: list[int] = [0, 0, 0]
sales_totals: list[float] = [0.0, 0.0, 0.0]

# Supermarket totals
total_transactions: int = 0
total_sales: float = 0.0

# Controls whether the program continues running
program_running: bool = True


print("=" * 50)
print("FRESHMART CASHIER TRANSACTION SYSTEM")
print("=" * 50)
