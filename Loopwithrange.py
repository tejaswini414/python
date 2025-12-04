total = 0
expenses = []
num_expenses = int(input("enter number of expenses:"))
for i in range(7):
    expenses.append(float(input("enter expenses:")))
total = sum(expenses)
print("Expense so far:$", total, sep = '')