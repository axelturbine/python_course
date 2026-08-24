import json

contacts = [
    {"name": "Axel", "phone": "070-123456", "city": "Malmö"},
    {"name": "Pjär", "phone": "072-987654", "city": "Jönköping"}
]

with open("contacts.json", "w") as file:
    json.dump(contacts, file)

print("Saved!")

with open("contacts.json", "r") as file:
    loaded_contacts = json.load(file)

print(loaded_contacts)