def get_valid_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Thats not a number! Please enter a valid number.")

result = get_valid_number("Which contact do you want to delete? ")
print(result)