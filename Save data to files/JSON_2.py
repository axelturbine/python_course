import json

try:
    with open("scores.json", "r") as file:
        scores = json.load(file)
except FileNotFoundError:
    scores = []

name = input("Enter your name: ")
score = int(input("Enter your score: "))

scores.append({"name": name, "score": score})
with open("scores.json", "w") as file:
    json.dump(scores, file)

for entry in scores:
    print(entry["name"], "-", entry["score"])