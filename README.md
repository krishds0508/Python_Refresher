# Python_Refresher
# Personal Expense Tracker

## Introduction

The Personal Expense Tracker is a command-line tool that allows users to log, categorize, and visualize their expenses. It provides functionalities for loading and saving data, setting budgets, and generating interactive reports.

## Prerequisites

Ensure you have the following installed before using this script:

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`)
- A valid expense data file (`expense_data_1.csv`)

## Installation

1. Clone or download the script to your local machine.
2. Navigate to the directory containing the script.
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

To execute the script, use:

```sh
python expense_tracker.py --help
```

This will display available options and their descriptions.

### Available Commands

#### 1. **Interactive Expense View**

Generate an interactive breakdown of expenses:

```sh
python expense_tracker.py --interactive-view
```

This command will visualize expenses by category using an interactive donut chart.

#### 2. **Loading Expenses from a CSV File**

To load expenses from a CSV file:

```sh
python expense_tracker.py --load-csv expense_data_1.csv
```

This loads expense data while preserving previous entries.

#### 3. **Saving Expenses to a CSV File**

To save the current expenses to a specified CSV file:

```sh
python expense_tracker.py --save expenses.csv
```

#### 4. **Adding a New Expense**

To add a new expense manually:

```sh
python expense_tracker.py --add 150 Food "Lunch at restaurant" 2025-03-15
```

This will add an expense of ₹150 categorized under "Food" with the description "Lunch at restaurant" on March 15, 2025.

#### 5. **Viewing Available Categories**

To see the list of predefined categories:

```sh
python expense_tracker.py --view-categories
```

#### 6. **Viewing Budget Allocations**

To view the budgets assigned to different categories:

```sh
python expense_tracker.py --view-budgets
```

#### 7. **Setting a Budget for a Category**

To set a budget for a specific category:

```sh
python expense_tracker.py --set-budget Food 5000
```

This sets a ₹5000 budget for the "Food" category.

## Example Output

### Expense Summary Table

After running `--interactive-view`, a table similar to the following will be displayed:

```
Expense Summary by Category (INR):
---------------------------------------------------------------
Category              Amount          Percentage    # Transactions
---------------------------------------------------------------
Food                 ₹12,500.00        25.0%        10
Transport            ₹ 6,000.00        12.0%         7
Shopping            ₹ 4,500.00         9.0%         5
---------------------------------------------------------------
Total               ₹50,000.00       100.0%        50
```

## Notes

- Ensure your CSV file follows the expected format with the columns `Date`, `Category`, `Note`, `Income/Expense`, and `Amount`.
- The script only considers rows where `Income/Expense` is marked as `Expense`.
- All transactions are converted to a numerical format for accurate calculations.

## Author
Krishna Prasad