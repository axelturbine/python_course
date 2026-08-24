while True:
    grade = int(input("What score did you get on the test? (0-100) "))
    if grade > 100 or grade < 0:
        print("Invalid score! Enter a number between 0 and 100.")
    elif grade >= 90 and grade <= 100:
        print("Grade: A")
        break
    elif grade >= 80:
        print("Grade: B")
        break
    elif grade >= 70:
        print("Grade: C")
        break
    elif grade < 70:
        print("Failed")
        break
    else:
        print("Too high number, try again!")