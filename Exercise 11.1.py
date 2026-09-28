# Movie Theatre Booking Simulator

seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

while True:
    print("\nMovie Theatre Seating:")
    print("  1 2 3")

    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            print(seats[i][j], end=" ")
        print()

    row = int(input("\nEnter row (1-3, 0 to exit): "))
    col = int(input("Enter column (1-3, 0 to exit): "))

    if row == 0 and col == 0:
        print("Thank you for using the booking system!")
        break

    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or column!")
    elif seats[row - 1][col - 1] == "X":
        print("Seat is already reserved!")
    else:
        seats[row - 1][col - 1] = "X"
        print("Seat reserved successfully!")