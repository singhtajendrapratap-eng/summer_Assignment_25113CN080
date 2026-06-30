#write a program to create mini library system.
books = []

while True:
    print("\n----- LIBRARY SYSTEM -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        book = input("Book Name: ")
        books.append(book)

    elif choice == 2:
        book = input("Book to Issue: ")
        if book in books:
            books.remove(book)
            print("Book Issued")
        else:
            print("Book not available")

    elif choice == 3:
        book = input("Book to Return: ")
        books.append(book)
        print("Book Returned")

    elif choice == 4:
        print("Books Available:")
        for b in books:
            print(b)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")