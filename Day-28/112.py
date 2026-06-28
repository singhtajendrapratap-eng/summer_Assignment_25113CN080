#write a program to create contact management system.
contacts = {}

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully.")

    elif choice == 2:
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found.")

    elif choice == 3:
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted.")
        else:
            print("Contact Not Found.")

    elif choice == 4:
        print("\nContact List")
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")