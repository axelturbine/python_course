movie = input("Write down your favorite movie: ")
with open("movies.txt", "a") as file:
    file.write("Favorite Movie: " + movie + "\n")

with open("movies.txt", "r") as file:
    content = file.read()
    print(content)