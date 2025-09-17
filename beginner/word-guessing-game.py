import random

name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the Word Guessing Game!")

words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer', 'function', 'variable', 'condition']
word = random.choice(words)

print("Guess the characters!")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        
        else:
            print("_")
            failed += 1

    if failed == 0:
        print(f"\nCongratulations, {name}! You guessed the word '{word}' correctly!")
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -=1
        print(f"Wrong guess. You have {turns} more guesses.")

        if turns == 0:
            print(f"Sorry, {name}. You've run out of guesses. The word was '{word}'. Better luck next time!")