import json

movies = [
    {"title": "Star Wars"},
    {"title": "The Matrix"},
    {"title": "Interstellar"}
]

with open("movies.json", "w") as file:
    json.dump(movies, file)

with open("movies.json", "r") as file:
    loaded_movies = json.load(file)

for movie in loaded_movies:
    print(movie["title"])