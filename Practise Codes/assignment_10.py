friends = [
    { "Name": "Linus", "Age": 25 },
    { "Name": "Malva", "Age": 18 },
    { "Name": "Abbe", "Age": 16 }
]
for friend in friends:
    if friend["Age"] >= 18:
        print(friend["Name"], "is an adult!" )
    else:
        print(friend["Name"], "is not an adult yet!")
