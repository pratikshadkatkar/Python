# Daily Class Schedule

days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

schedule = [
    ["Math", "Physics", "English", "Chemistry", "Computer", "Free", "Free"],
    ["English", "Math", "Computer", "Physics", "Chemistry", "Free", "Free"],
    ["Computer", "English", "Math", "Chemistry", "Physics", "Free", "Free"],
    ["Physics", "Computer", "Chemistry", "Math", "English", "Free", "Free"],
    ["Chemistry", "Physics", "Computer", "English", "Math", "Free", "Free"]
]

while True:
    print("\n========== CLASS SCHEDULE ==========")

    print("       ", end="")
    for day in days:
        print(f"{day:<12}", end="")
    print()

    for i in range(5):
        print(f"Hour {i + 1:<2}", end=" ")
        for j in range(7):
            print(f"{schedule[i][j]:<12}", end="")
        print()

    print("\nEnter hour (1-5) and day (1-7) to change a subject.")
    print("Enter 0 0 to exit.")

    row = int(input("Enter hour: "))
    col = int(input("Enter day: "))

    if row == 0 and col == 0:
        print("Exiting schedule...")
        break

    if row < 1 or row > 5 or col < 1 or col > 7:
        print("Invalid hour or day!")
    else:
        subject = input("Enter new subject: ")

        schedule[row - 1][col - 1] = subject

        print("Schedule updated successfully!")