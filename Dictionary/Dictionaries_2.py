friends = []
for i in range(3):
    friend = input("Enter a friend's name: ")
    age = int(input("Enter their age: "))
    friends.append({"name": friend, "age": age})

for friend in friends:
    print(friend["name"], "is", friend["age"], "years old.")