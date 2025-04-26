import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added.")

def list_contacts():
    contacts = load_contacts()
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")

def search_contact():
    name = input("Enter name to search: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if name in c["name"].lower()]
    for c in found:
        print(f"{c['name']} - {c['phone']} - {c['email']}")
    if not found:
        print("No contacts found.")

def main():
    while True:
        print("\n[1] Add [2] List [3] Search [4] Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
