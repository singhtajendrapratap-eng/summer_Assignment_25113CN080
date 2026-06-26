#write a program to create number guessing game.
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess (1-100): "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too Low!")
    else:
        print("Too High!")