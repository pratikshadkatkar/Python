transaction = []

for i in range(5):
    amount = float(input( f"Enter transaction { i + 1}:"))
    transaction.append(amount)

largest = max(transaction)
average = sum(transaction) / len(transaction)

print("\nTransaction List:", transaction)
print("Largest Transaction:", largest)
print("Average Spend:", average)