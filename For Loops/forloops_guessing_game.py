import random
secret = random.randint(1, 10)
guess = 0
print("I'm thinking of a number between 1 and 10.")
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("You got it!")
    if guess < secret:
        print("Too low!")
    if guess > secret:
        print("Too high!")