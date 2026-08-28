import json

with open("students.json", "r") as file:
    students = json.load(file)

print(students)

total = 0
for student in students:
    total += student["grade"]
average = total / len(students)
print("Class average:", average)

print("\nAbove average")
for student in students:
    if student["grade"] > average:
        print("-", student["name"], ":", student["grade"])

print("\nBelow average")
for student in students:
    if student["grade"] < average:
        print("-", student["name"], ":", student["grade"])