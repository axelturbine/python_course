try:
    with open("secret.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
    with open("secret.txt", "w") as file:
        file.write("This is the default message!\n")
    print("Created a new file with a default message!")