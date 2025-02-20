"""
Personal Expense Tracker

Author: Krishna Prasad
Date:   2025_02_12

This script allows users to manage personal expenses by adding, viewing, and analyzing expenses.
It supports loading and saving data from CSV files, setting budgets, and visualizing expenses
through an interactive dashboard.
"""

import json
import os
import argparse
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def default_categories():
    """
    Returns a list of default expense categories.

    Returns:
        list: A list of predefined expense categories.
    """
    return ["Food", "Transport", "Shopping", "Entertainment", "Grocery", "Healthcare", "Utilities", "Rent", "Savings", "Miscellaneous"]

def load_expenses(file_name):
    """
    Loads expenses from a JSON file.

    Args:
        file_name (str): The path to the JSON file containing expense data.

    Returns:
        dict: A dictionary containing expenses and budgets. If the file does not exist, returns an empty structure.
    """
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to load JSON. Initializing empty records.")
    return {"expenses": [], "budgets": {}}

def save_expenses_to_csv(data, file_name):
    """
    Saves expenses to a CSV file, ensuring new entries are appended instead of overwriting existing data.

    Args:
        data (dict): The dictionary containing expenses and budgets.
        file_name (str): The path to the CSV file where data should be saved.
    """
    existing_data = load_expenses_from_csv(file_name)
    new_entries = [expense for expense in data["expenses"] if expense not in existing_data]
    if new_entries:
        existing_data.extend(new_entries)
        df = pd.DataFrame(existing_data)
        df.to_csv(file_name, index=False)
        print(f"New expenses added and saved to {file_name}")
    else:
        print("No new expenses to add.")

def interactive_expense_view(data):
    """
    Displays an interactive expense breakdown using a donut chart and prints a summary table.

    Args:
        data (dict): The dictionary containing expenses and budgets.
    """
    df = pd.read_csv("expense_data_1.csv")
    df = df[df['Income/Expense'].str.lower() == 'expense']
    
    if df.empty:
        print("No expenses to display.")
        return
    
    primary_currency = df['Currency'].mode().iloc[0]
    category_expenses = df.groupby('Category')['Amount'].sum().reset_index()
    category_expenses = category_expenses.sort_values('Amount', ascending=False)
    total_expense = category_expenses['Amount'].sum()
    
    category_expenses['Percentage'] = (category_expenses['Amount'] / total_expense * 100).round(2)
    category_expenses['Label'] = category_expenses.apply(
        lambda x: f"{x['Category']}\n{x['Percentage']:.1f}%", axis=1
    )
    
    fig = go.Figure(data=[go.Pie(
        labels=category_expenses['Label'],
        values=category_expenses['Amount'],
        hole=0.4,
        textinfo='label',
        hovertemplate="Category: %{label}<br>Amount: ₹%{value:,.2f}<extra></extra>",
        textposition='inside',
    )])
    
    fig.update_layout(
        title=f"Expense Breakdown by Category ({primary_currency})",
        showlegend=True,
        width=1200,
        height=800,
    )
    
    fig.show()
    
    # Print a summary table
    print(f"\nExpense Summary by Category ({primary_currency}):")
    print("-" * 65)
    print(f"{'Category':<20} {'Amount':<15} {'Percentage':<12} {'# Transactions':<15}")
    print("-" * 65)
    
    transaction_counts = df['Category'].value_counts()
    for _, row in category_expenses.iterrows():
        category = row['Category']
        amount = row['Amount']
        percentage = row['Percentage']
        count = transaction_counts.get(category, 0)
        print(f"{category:<20} ₹{amount:>12,.2f} {percentage:>10.1f}% {count:>14}")
    
    print("-" * 65)
    print(f"{'Total':<20} ₹{total_expense:>12,.2f} {100:>10.1f}% {len(df):>14}")

def main():
    """
    Handles command-line arguments and executes the corresponding functions.
    """
    parser = argparse.ArgumentParser(description="Personal Expense Tracker")
    parser.add_argument("--interactive-view", action="store_true", help="Display an interactive breakdown of expenses")
    args = parser.parse_args()
    
    data = load_expenses("expenses.json")
    
    if args.interactive_view:
        interactive_expense_view(data)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
