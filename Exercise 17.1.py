
import secrets

def roll_dice():
    print("=== Secure Multi-Dice Rolling Simulator ===")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))

            # Validate user input
            if num_dice < 1:
                print("Please enter a number greater than 0.")
            elif num_dice > 1000:
                print("You can roll a maximum of 1000 dice at once.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Generate secure random outcomes (1–6)
    results = [secrets.randbelow(6) + 1 for _ in range(num_dice)]

    # Calculate the total score
    total_score = sum(results)

    # Display the results
    print("\n--- Dice Roll Results ---")
    for index, result in enumerate(results, start=1):
        print(f"Die {index}: {result}")

    print(f"\nNumber of dice: {num_dice}")
    print(f"Total score: {total_score}")


if __name__ == "__main__":
    roll_dice()