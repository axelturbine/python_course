attempts = 0
secret_number = 42
while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        print("It took you", attempts + 1, "attempts to guess the number.")
        break
    else:
        print("Try again.")
    attempts += 1