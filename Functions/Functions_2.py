def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

conversion = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ")
temperature = int(input("Enter the temperature: "))

if conversion == "C":
    result = celsius_to_fahrenheit(temperature)
    print(temperature, "°C is equal to", result, "°F")
elif conversion == "F":
    result = fahrenheit_to_celsius(temperature)
    print(temperature, "°F is equal to", result, "°C")