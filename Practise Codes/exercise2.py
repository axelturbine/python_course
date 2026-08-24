while True:
    try:
        number = int(input("Enter a number between 1-10: "))
        if number >= 1 and number <= 10:
            print("Success")
            break
        else:
            print("Nice try, give it another go!")
    except ValueError:
        print("Thats not a number! Try again")