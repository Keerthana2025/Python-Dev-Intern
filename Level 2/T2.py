//NUMBER GUESSING

import random

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

number = random.randint(lower, upper)

guess = None
attempts = 0

print(f"\n I have selected a number between {lower} and {upper}. Can you guess it?")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
