secret = "python"
guess = 0
print("Im thinking of a random word.")
attempts = 0
while guess != secret:
    guess = input("Guess the secret word: ")
    if guess == secret:
        print("You got it!")
        break
    else:
        print("That's wrong, try again!")
    attempts = attempts + 1

print("It took you", attempts + 1, "attempts!")