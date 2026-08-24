import json

songs = [
    {"Song Title": "One Dance", "Artist": "Drake"},
    {"Song Title": "Flashing Lights", "Artist": "Kanye West"}
]

with open("songs.json", "w") as file:
    json.dump(songs, file)

print("Saved")

with open("songs.json", "r") as file:
    loaded_songs = json.load(file)

for song in loaded_songs:
    print(song["Song Title"], "by", song["Artist"])
