def calculate(number1, number2, operation):
    if operation == "add":
        result = number1 + number2
    elif operation == "subtract":
        result = number1 - number2
    elif operation == "multiply":
        result = number1 * number2
    else:
        print("Unknown operation")
        return None
    return result

print(calculate(5, 3, "add"))
print(calculate(10, 4, "subtract"))
print(calculate(6, 7, "multiply"))
print(calculate(5, 3, "divide"))