text = input("Enter the email text: ")

symbols = "@.!"
count = 0

for ch in text:
    if ch in symbols:
        count += 1

print("Number of special symbols:", count)