import random

def guess_number():
    print("Welcome to my number guessing game!")

    answer = random.randint(1, 200)
    attempts = 10

    while attempts > 0:
        guess = int(input("Guess a number between 1 and 200: "))

        if guess < answer:
            print("Your guess is too low!")
        elif guess > answer:
            print("Your guess is too high!")
        else:
            print(f"Congratulations! You guessed the number in {10 - attempts + 1} attempts.")
            return

        attempts -= 1

    print(f"Sorry, you've run out of attempts. The correct number was {answer}.")

guess_number()

