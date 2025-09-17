import random

print("Hi! Welcome to the Number Guessing Game! \n You have to guess a number between 1 and 100. \n You have 7 attempts. Good luck!")

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

print(f"\n You have 7 chances to guess the number between {low} and {high}. Let's begin!")

num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))
    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} attempts.")
        break
    elif gc >= ch and guess != num:
        print(f"Sorry, you've used all your attempts. The number was {num}. Better luck next time!")
    elif guess < num:
        print("Too low! Try a higher number.")
    elif guess > num:
        print("Too high! Try a lower number.")
