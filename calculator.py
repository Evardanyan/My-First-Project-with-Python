 Earned amounts for each item
earnings = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

print("Earned amount:")
total_income = sum(earnings.values())  # Calculate the total income directly

# Print the earned amount for each item
for item, amount in earnings.items():
    print(f"{item}: ${amount}")

# Print the total income
print(f"\nIncome: ${total_income}")

# Retrieve staff expenses from the user
staff_expenses = int(input("Staff expenses:\n "))

# Retrieve other expenses from the user
other_expenses = int(input("Other expenses:\n "))

# Calculate and print the net income
net_income = total_income - staff_expenses - other_expenses
print(f"Net income: ${net_income}")
