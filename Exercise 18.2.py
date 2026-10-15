filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        count = 0

        print("\nFile Contents:")

        for line in f:
            print(line, end="")
            count += 1

        print("\nTotal number of lines:", count)

except FileNotFoundError:
    print("File not found!")