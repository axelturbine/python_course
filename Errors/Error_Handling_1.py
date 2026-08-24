while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))
        if number >= 1 and number <= 10:
            print("Great choice! You entered:", number)
            break
        else:
            print("That's not a number between 1 and 10! Please try again.")
    except ValueError:
        print("That's not a number! Please enter a valid number.")
