from colorama import Fore, Style

import json

def get_valid_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print(Fore.RED + "Thats not a number! Please enter a valid number." + Style.RESET_ALL)

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def show_contacts(contacts):
    if len(contacts) == 0:
        print(Fore.RED + "No contacts yet!" + Style.RESET_ALL)
    else:
        for index, contact in enumerate(contacts):
            print(index + 1, "- Name", contact["name"], "| Phone", contact["phone"], "| City:", contact["city"])

def add_contact(contacts):
    name = input("Add name: ")
    phone = input("Add phone number: ")
    city = input("Add city: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "city": city
        })
    print(Fore.GREEN + "Contact added!" + Style.RESET_ALL)

def delete_contact(contacts):
    if len(contacts) == 0:
        print(Fore.RED + "No contacts yet!" + Style.RESET_ALL)
    else:
        for index, contact in enumerate(contacts):
            print(index + 1, "-", contact["name"])
        number = get_valid_number("Which contact should i delete? ")
        contacts.pop(number - 1)
        print(Fore.GREEN + "Contact removed!" + Style.RESET_ALL)
        
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

while True:
    print(Fore.BLUE + "--- Contact Book ---" + Style.RESET_ALL)
    print("1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(contacts)
        save_contacts(contacts)
    elif choice == "2":
        show_contacts(contacts)
    elif choice == "3":
        delete_contact(contacts)
        save_contacts(contacts)
    elif choice == "4":
        print("Goodbye!")
        break
