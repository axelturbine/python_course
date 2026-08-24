import random

words = ["python", "computer", "keyboard", "skateboard", "programming", "developer"]
secret_word = random.choice(words)

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

guessed_letters = []
display = []

for letter in secret_word:
    display.append("_")

attempts = 6

while attempts > 0:
    print(" ".join(display))
    print("Attempts remaining:", attempts)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print(hangman_stages[6 - attempts])
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter!")
        continue

    if guess in secret_word:
        print("correct")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        if guess not in guessed_letters:    
            guessed_letters.append(guess)
            attempts -= 1

    if "_" not in display and len(display) > 0:
        print("Attempts remaining:", attempts)
        print(hangman_stages[6 - attempts])
        print("You won! The word was:", secret_word)
        break

if attempts == 0:
    print("Attempts remaining:", attempts)
    print(hangman_stages[6 - attempts])
    print("You lost! The word was:", secret_word)
