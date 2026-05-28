import json
import os

FILE_NAME = "contacts.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)

else:
    contacts = {}
choice = 0

print ("1. Add")
print ("2. View")
print ("3. Delete")
print ("4. Exit")

while choice != 4:
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = int(input("Enter phone: "))
        
        contacts[name] = phone
        print (f'Contact {name} was added successfully.')
    
    elif choice == 2:
        for name, phone in contacts.items():
            print(f'Phone: {phone} | Name: {name}')
        
    elif choice == 3:
        pop = input("Enter the name u want to remove: ")
        contacts.pop(pop, None)
        print(f"Removed {pop} if they existed.")
    
    elif choice > 4:
        print("invalid choice")
    
    elif choice == 4:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file)
        print("Exiting...")
        break