while True:
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        result = number1 / number2
        print("The result of dividing", number1, "by", number2, "is:", result)
        break
    except ValueError:
        print("That's not a number! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero second number.")