with open ("shopping.txt", "w") as file:
    file.write("Milk\n")
    file.write("Bread\n")
    file.write("Eggs\n")
    file.write("Chicken\n")
    file.write("Rice\n")

with open("shopping.txt", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        print(index + 1, ".", line)
