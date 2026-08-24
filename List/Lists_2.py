names = []
for i in range(4):
    name = input("Enter a name: ")
    names.append(name)

names.reverse()
for name in names:
    print(name)