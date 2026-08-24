while True:
    try:
        number1 = int(input("Write a number: "))
        number2 =int(input("Write a second number: "))
        result = number1 / number2
        print("Result: ", result)
        break
    except ValueError:
        print("Write down a number, not a letter!")
    except ZeroDivisionError:
        print("Devide with something else than 0!")