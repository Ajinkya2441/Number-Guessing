import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Choose difficulty: easy / medium / hard")
    level = input("Your choice: ").lower()

    if level == "easy":
        max_attempts = 10
    elif level == "medium":
        max_attempts = 7
    elif level == "hard":
        max_attempts = 5
    else:
        print("Invalid choice. Defaulting to medium.")
        max_attempts = 7

    number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts+1}/{max_attempts} - Your guess: ")
        if not guess.isdigit():
            print("❌ Invalid input. Enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print(f"🎉 You guessed it in {attempts} tries!")
            break
        elif guess < number:
            print("🔼 Too low.")
        else:
            print("🔽 Too high.")

    else:
        print(f"😢 You're out of attempts! The number was {number}.")

while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break
