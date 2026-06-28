#write a program to create library management system.
library = {}

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library[book] = "Available"
        print("Book added successfully.")

    elif choice == 2:
        book = input("Enter book name to issue: ")
        if book in library and library[book] == "Available":
            library[book] = "Issued"
            print("Book issued successfully.")
        else:
            print("Book not available.")

    elif choice == 3:
        book = input("Enter book name to return: ")
        if book in library:
            library[book] = "Available"
            print("Book returned successfully.")
        else:
            print("Book not found.")

    elif choice == 4:
        print("\nBooks List:")
        if len(library) == 0:
            print("No books available.")
        else:
            for book, status in library.items():
                print(book, "-", status)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")