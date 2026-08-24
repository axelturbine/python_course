import json

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def status(self):
        if self.grade >= 60:
            print(f"{self.name} has passed!")
        else:
            print(f"{self.name} has failed.")

students = [
    Student("Elin", 75),
    Student("Filip", 90),
    Student("Fatima", 20)
]

for student in students:
    student.status()

students_data = []
for student in students:
    students_data.append({"name": student.name, "grade": student.grade})

with open("students.json", "w") as file:
    json.dump(students_data, file)

print("Saved to students.json!")