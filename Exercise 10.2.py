products = ["Laptop", "Mobile", "Mouse", "Keyboard", "Printer"]

item = input("Enter item name: ")

if item in products:
    print("Item found!")
    print("Index:", products.index(item))
else:
    print("Item is not found!")