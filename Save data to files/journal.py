note = input("Write a note! ")
with open("journal.txt", "a") as file:
    file.write("Note: " + note + "\n")
    file.write("Thank you for sharing!\n")

with open("journal.txt", "r") as file:
    content = file.read()
    print(content)