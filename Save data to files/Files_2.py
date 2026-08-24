while True:
    print("---- Notes ----")
    print("1. Add note")
    print("2. View notes")
    print("3. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        note = input("Write your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
    elif choice == 2:
        try:
            with open("notes.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("No notes yet!")
    elif choice == 3:
        print("Exiting program!")
        break 