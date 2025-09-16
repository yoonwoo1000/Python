import random


def main():
    print("UpDown.py is running")

    while True:
        startInput = input("Do you want to start the UpDown game? (y/n): ")
        if startInput.strip().lower() == "n":
            exit()
        elif startInput.strip().lower() == "y":
            print("Starting the UpDown game!")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue

        target = random.randint(1, 100)
        numberList = []
        while True:
            print(f"Your previous guesses: {numberList}")

            userInput = input("Enter a number between 1 and 100 (or 'q' to quit): ")

            if userInput == "q":
                print("Exiting the game. Goodbye!")
                return
            elif userInput.isdigit():
                number = int(userInput)
                if number < 1 or number > 100:
                    print("Please enter a number within the range of 1 to 100.")
                    continue
                elif number < target:
                    print("Up!")
                    numberList.append(number)
                elif number > target:
                    print("Down!")
                    numberList.append(number)
                else:
                    print("Correct! You've guessed the number.")
                    return
            else:
                print("Invalid input. Please enter a valid number or 'q' to quit.")
                continue


if __name__ == "__main__":
    main()
