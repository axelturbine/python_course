todos = []

while True:
    print("--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    print("4. Mark as done")
    print("5. Delete task")
    choice = input("Choose an option: ")
    if choice == "3":
        print("Goodbye!")
        break
    elif choice == "1":
        task = input("Enter a task: ")
        todos.append({"task": task, "done": False})
        print("Task added!")
    elif choice == "2":
        if len(todos) == 0:
               print("No tasks yet!")
        else:
             for todo in todos:
                if todo["done"]:
                    print("✓", todo["task"])
                else:
                    print("✗", todo["task"])
    elif choice == "4":
        for index, todo in enumerate(todos):
            print(index + 1, "-", todo["task"])
        number = int(input("Which task is done? "))
        todo = todos[number - 1]
        todo["done"] = True
        # [todos[number - 1]"done"] = True
        print("Task marked as done!")
    elif choice == "5":
        for index, todo in enumerate(todos):
            print(index + 1, "-", todo["task"])
        number = int(input("Which task should i delete? "))
        todos.pop(number - 1)
        print("Task is removed!")
        