age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 17:
    print("Teenager")
elif age >= 18 and age < 64:
    print("Adult")
else: 
    print("Senior")