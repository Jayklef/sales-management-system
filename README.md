# sales-management-system
An automated sales management system project
# FreshMart Automated Sales Management System

## Project Overview

FreshMart Supermarket currently records sales manually. This process is slow, can produce incorrect totals, and makes it difficult to prepare accurate end-of-day reports.

This project is a command-line Python application that records transactions for three pre-registered cashiers and automatically generates a daily sales report.

## Pre-registered Cashiers

The application contains three cashiers:

1. Sarah
2. David
3. Grace

The operator selects one of these cashiers whenever a new transaction is recorded.

## Features

- Records transactions one at a time
- Assigns each transaction to a cashier
- Validates cashier selections
- Validates transaction amounts
- Classifies transactions as small, regular, or high-value
- Tracks each cashier's transaction count
- Tracks each cashier's total sales
- Calculates each cashier's average transaction
- Tracks the supermarket's total transactions and sales
- Generates an end-of-day report
- Stores information in memory while the program runs

## Transaction Categories

| Category | Amount |
| --- | ---: |
| Small transaction | Below ₦10,000 |
| Regular transaction | ₦10,000 to ₦99,999.99 |
| High-value transaction | ₦100,000 or more |

> **Note:** The project brief shows ₦8,000 as a small transaction and ₦25,000 as a regular transaction, but it does not state every classification boundary. The limits can be changed if different values are provided.

## Requirements

- Python 3.9 or newer
- Visual Studio Code or another code editor
- No third-party Python packages

## Project Structure

```text
freshmart_sales/
├── app.py
└── README.md
```

- `app.py` contains the Python application.
- `README.md` contains the project documentation.

## How to Run the Application

1. Open the project folder in Visual Studio Code.
2. Select **Terminal → New Terminal**.
3. Check that Python is installed:

```bash
python --version
```

4. Run the application:

```bash
python app.py
```

If your computer uses `python3`, run:

```bash
python3 app.py
```

## How the Application Works

When the application starts, it asks:

```text
Do you want to register a new transaction? Yes or No:
```

If the user enters `Yes`, the three cashiers are displayed:

```text
1. Sarah
2. David
3. Grace
```

The user then:

1. Selects a cashier.
2. Enters a transaction amount.
3. Receives the transaction classification.
4. Chooses whether to record another transaction.

When the user enters `No`, the application generates the end-of-day report and stops running.

## Sample Test Data

Use these transactions to reproduce the example in the project brief:

| Cashier | Amount | Classification |
| --- | ---: | --- |
| Sarah | ₦25,000 | Regular |
| Sarah | ₦8,000 | Small |
| Grace | ₦150,000 | High-value |

After recording the transactions, enter `No`.

## Expected Cashier Results

| Cashier | Transactions | Total Sales | Average |
| --- | ---: | ---: | ---: |
| Sarah | 2 | ₦33,000.00 | ₦16,500.00 |
| David | 0 | ₦0.00 | ₦0.00 |
| Grace | 1 | ₦150,000.00 | ₦150,000.00 |

## Expected Supermarket Results

```text
Total Transactions: 3
Total Daily Sales: ₦183,000.00
Average Transaction: ₦61,000.00
```

## Python Concepts Demonstrated

- Variables and constants
- Strings
- Integers
- Floating-point numbers
- Boolean values
- Lists and list indexes
- Type hints
- Docstrings
- `input()` and `print()`
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- `if`, `elif`, and `else`
- `while` loops
- Input validation
- `try` and `except`
- Formatted strings
- Currency formatting

## Data Storage

The application uses three parallel lists:

```python
cashier_names = ["Sarah", "David", "Grace"]
transaction_counts = [0, 0, 0]
sales_totals = [0.0, 0.0, 0.0]
```

Values at the same index belong to the same cashier:

| Index | Cashier | Transaction Count | Sales Total |
| ---: | --- | ---: | ---: |
| `0` | Sarah | `transaction_counts[0]` | `sales_totals[0]` |
| `1` | David | `transaction_counts[1]` | `sales_totals[1]` |
| `2` | Grace | `transaction_counts[2]` | `sales_totals[2]` |

For example, Sarah's information is stored at index `0`:

```python
cashier_names[0]
transaction_counts[0]
sales_totals[0]
```

All information is stored in memory. The information disappears when the application closes.

## Input Validation

The application checks that:

- The user enters `Yes`, `Y`, `No`, or `N`.
- The cashier number is `1`, `2`, or `3`.
- The cashier number is a whole number.
- The transaction amount is numeric.
- The transaction amount is greater than zero.

If invalid information is entered, the application displays an error message and asks the user to try again.

## Average Calculations

A cashier's average transaction is calculated as:

```text
Cashier total sales ÷ Cashier transaction count
```

The supermarket average is calculated as:

```text
Total daily sales ÷ Total supermarket transactions
```

The application checks that the transaction count is greater than zero before dividing. This prevents a division-by-zero error.

## Current Limitations

- Data is not saved after the program closes.
- The application supports only three cashiers.
- Cashier names are written directly into the program.
- Individual transactions are not stored separately.
- Transaction dates and IDs are not recorded.
- The application does not use a database.
- Reports are only displayed in the terminal.

## Possible Future Improvements

- Save individual transactions to a CSV file
- Store transactions in a SQLite database
- Add transaction dates and identifiers
- Generate weekly and monthly reports
- Add automated tests
- Separate the application into multiple Python modules
- Use functions to reduce repeated code
- Use SQL to calculate totals and averages
- Export the daily report to a file

## Author

**Name:** Add your name here  
**Project:** Python Capstone Project  
**Application:** FreshMart Automated Sales Management System
