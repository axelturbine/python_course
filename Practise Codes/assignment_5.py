color = "blue"
guess = ""
while guess != color:
    guess = input("Guess the color: ")
    if guess == color:
        print("You guessed it!")
    else:
        print("Wrong guess! Try again.")