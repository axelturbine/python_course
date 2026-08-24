attempts = 0
while True:
    word = input("Enter a word: ")
    if word == "stop":
        print("Stopping the loop.")
        print("You entered", attempts, "words before stopping,")
        break
    else:
        print("You entered:", word)
        attempts += 1