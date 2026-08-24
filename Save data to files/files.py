file = open("notes.txt", "w")
file.write("Hello, this is my first file!\n")
file.write("This is a second line!\n")
file.close()

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)