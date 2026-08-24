goal = input("Write a daily goal! ")
with open("goals.txt", "a") as file:
    file.write("Daily goal: " + goal + "\n")

with open("goals.txt", "r") as file:
    content = file.read()
    print(content)