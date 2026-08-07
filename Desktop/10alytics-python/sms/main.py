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


while program_running:
    response: str = input(
        "\nDo you want to register a new transaction? Yes or No: "
    ).strip().lower()

    if response == "yes" or response == "y":
        print("\nSelect the cashier:")

        print(f"1. {cashier_names[0]}")
        print(f"2. {cashier_names[1]}")
        print(f"3. {cashier_names[2]}")

        cashier_is_valid: bool = False

        while not cashier_is_valid:
            try:
                cashier_number: int = int(
                    input("\nEnter cashier number: ")
                )

                if cashier_number >= 1 and cashier_number <= 3:
                    cashier_is_valid = True
                else:
                    print("Invalid cashier number. Enter 1, 2, or 3.")

            except ValueError:
                print("Invalid input. Enter a whole number.")

        # Convert the user's selection to a list index.
        # Cashier 1 uses index 0, cashier 2 uses index 1, and so on.
        cashier_index: int = cashier_number - 1

        amount_is_valid: bool = False

        while not amount_is_valid:
            try:
                amount_input: str = input(
                    "Enter transaction amount: "
                ).strip()

                # Allows the user to enter 25000 or 25,000
                amount_input = amount_input.replace(",", "")

                transaction_amount: float = float(amount_input)

                if transaction_amount > 0:
                    amount_is_valid = True
                else:
                    print(
                        "Transaction amount must be greater than zero."
                    )

            except ValueError:
                print(
                    "Invalid amount. Enter a number such as 25000."
                )

        # Update the selected cashier's information
        transaction_counts[cashier_index] += 1
        sales_totals[cashier_index] += transaction_amount

        # Update the supermarket's information
        total_transactions += 1
        total_sales += transaction_amount

        # Classify the transaction
        if transaction_amount < 10_000:
            print("\nSmall Transaction")

        elif transaction_amount >= 100_000:
            print("\nHigh-value Transaction")

        else:
            print("\nRegular Transaction")

        print("Transaction recorded successfully.")

    elif response == "no" or response == "n":
        program_running = False

    else:
        print("Invalid response. Please enter Yes or No.")


print("\n" + "=" * 50)
print("FRESHMART DAILY CASHIER REPORT")
print("=" * 50)


# Calculate Sarah's average
if transaction_counts[0] > 0:
    cashier_1_average: float = (
        sales_totals[0] / transaction_counts[0]
    )
else:
    cashier_1_average = 0.0


print(f"\nCASHIER 1: {cashier_names[0]}")
print(
    f"Transactions Processed: {transaction_counts[0]}"
)
print(f"Total Sales: ₦{sales_totals[0]:,.2f}")
print(
    f"Average Transaction: ₦{cashier_1_average:,.2f}"
)
print("-" * 50)


# Calculate David's average
if transaction_counts[1] > 0:
    cashier_2_average: float = (
        sales_totals[1] / transaction_counts[1]
    )
else:
    cashier_2_average = 0.0


print(f"\nCASHIER 2: {cashier_names[1]}")
print(
    f"Transactions Processed: {transaction_counts[1]}"
)
print(f"Total Sales: ₦{sales_totals[1]:,.2f}")
print(
    f"Average Transaction: ₦{cashier_2_average:,.2f}"
)
print("-" * 50)


# Calculate Grace's average
if transaction_counts[2] > 0:
    cashier_3_average: float = (
        sales_totals[2] / transaction_counts[2]
    )
else:
    cashier_3_average = 0.0


print(f"\nCASHIER 3: {cashier_names[2]}")
print(
    f"Transactions Processed: {transaction_counts[2]}"
)
print(f"Total Sales: ₦{sales_totals[2]:,.2f}")
print(
    f"Average Transaction: ₦{cashier_3_average:,.2f}"
)
print("-" * 50)


# Calculate the supermarket's average transaction
if total_transactions > 0:
    supermarket_average: float = (
        total_sales / total_transactions
    )
else:
    supermarket_average = 0.0


print("\n" + "=" * 50)
print("OVERALL SUPERMARKET REPORT")
print("=" * 50)

print(f"\nTotal Transactions: {total_transactions}")
print(f"Total Daily Sales: ₦{total_sales:,.2f}")
print(
    f"Average Transaction: ₦{supermarket_average:,.2f}"
)

print("\n" + "=" * 50)
print("END OF BUSINESS DAY")
print("=" * 50)