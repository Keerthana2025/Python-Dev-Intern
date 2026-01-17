//GUESSING RANDOM GAME

import random

number = random.randint(1, 100)

guess = 0

while guess != number:
    guess = int(input("Guess the number (1 to 100): "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Congratulations! You guessed it right.")
