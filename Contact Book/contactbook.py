contacts = []

while True:
    print("--- Contact Book ---")
    print("1. Add contacts")
    print("2. Veiw all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Add name: ")
        phone = input("Add phone number: ")
        city = input("Add city: ")
        contacts.append({
            "name": name,
            "phone": phone,
            "city": city
    })
        print("Contact added!")

    elif choice == "5":
        print("Exiting program!")
        break

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet!")
        else:
            for index, contact in enumerate(contacts):
                print(index + 1, "- Name:", contact["name"], "| Phone:", contact["phone"], ",| City:", contact["city"])

    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts yet!")
        else:
            for index, contact in enumerate(contacts):
                print(index + 1, "-", contact["name"])
            number = int(input("Which contact should i delete? "))
            contacts.pop(number - 1)
            print("Contact removed!")

    elif choice == "3":
        name = input("Search for a name: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                print("Found! Name:", contact["name"], "| Phone:", contact["phone"], "| City:", contact["city"])
                found = True
        if found == False:
            print("Contact not found!")
            