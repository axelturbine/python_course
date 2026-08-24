# 🐍 Axel's Python Cheat Sheet
*Everything you've learned so far — keep this handy!*

---

## 1. Print & Variables
```python
print("Hello, world!")        # show something on screen

name = "Axel"                 # string (text)
age = 19                      # integer (whole number)
price = 9.99                  # float (decimal number)
is_cool = True                # boolean (True or False)
```

---

## 2. User Input
```python
name = input("What is your name? ")        # always returns a string
age = int(input("How old are you? "))      # convert to number with int()
```

---

## 3. Math
```python
10 + 5    # addition       → 15
10 - 5    # subtraction    → 5
10 * 5    # multiplication → 50
10 / 5    # division       → 2.0
10 % 3    # modulo         → 1 (remainder)
```

---

## 4. If / Elif / Else
```python
if age >= 18:
    print("Adult!")
elif age >= 13:
    print("Teenager!")
else:
    print("Child!")
```

### Comparison operators
```python
==   # equal to
!=   # not equal to
>    # greater than
<    # less than
>=   # greater than or equal to
<=   # less than or equal to
```

---

## 5. While Loop
```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
# prints 1, 2, 3, 4, 5
```

---

## 6. For Loop
```python
for number in range(1, 6):
    print(number)
# prints 1, 2, 3, 4, 5 (stops BEFORE 6!)

for fruit in fruits:
    print(fruit)
# loops through a list
```

---

## 7. Lists
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])        # apple (starts at 0!)
fruits.append("mango")  # add to end
print(len(fruits))      # number of items
fruits.pop(0)           # remove item at position 0
```

---

## 8. Dictionaries
```python
person = {
    "name": "Axel",
    "age": 19,
    "city": "Malmö"
}
print(person["name"])       # access a value
person["job"] = "IT intern" # add a new key

for key in person:          # loop through
    print(key, ":", person[key])
```

---

## 9. Lists of Dictionaries
```python
contacts = [
    {"name": "Axel", "phone": "070-123456"},
    {"name": "Sara", "phone": "070-654321"}
]
for contact in contacts:
    print(contact["name"], "-", contact["phone"])
```

---

## 10. Functions
```python
def greet(name):            # define a function
    print("Hello", name)

greet("Axel")               # call a function

def add(a, b):              # function with return value
    return a + b

result = add(5, 3)          # result = 8
```

---

## 11. Files
```python
# Write (overwrites everything)
with open("notes.txt", "w") as file:
    file.write("Hello!\n")

# Append (adds to end)
with open("notes.txt", "a") as file:
    file.write("New line!\n")

# Read
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 12. JSON
```python
import json

# Save a list/dictionary to a file
with open("data.json", "w") as file:
    json.dump(my_list, file)

# Load it back
with open("data.json", "r") as file:
    my_list = json.load(file)
```

---

## 13. Error Handling
```python
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a number! Try again.")

# Multiple errors
try:
    result = number1 / number2
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

---

## 14. Modules & Packages
```python
import math
import json
import random

from colorama import Fore, Style  # import specific parts

random.randint(1, 10)   # random number between 1 and 10
math.sqrt(16)           # square root → 4.0
math.pi                 # 3.14159...
round(3.7)              # → 4
```

---

## 15. Useful Built-in Functions
```python
len([1, 2, 3])          # → 3 (length)
max([1, 5, 3])          # → 5 (biggest)
min([1, 5, 3])          # → 1 (smallest)
int("19")               # → 19 (string to number)
str(19)                 # → "19" (number to string)
range(1, 6)             # → 1, 2, 3, 4, 5
enumerate(my_list)      # → index + item
```

---

## Projects you've built ✅
- Interactive calculator
- Number guessing game
- To-do list app
- Contact book app (with file saving!)

---

*Keep going Axel — du klarar det här! 💪🐍*
