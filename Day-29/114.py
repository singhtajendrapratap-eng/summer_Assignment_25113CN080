#write a program to create menu driven array operations.
arr = []

while True:
    print("\n----- ARRAY OPERATIONS -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter number: "))
        arr.append(x)

    elif choice == 2:
        x = int(input("Enter number to delete: "))
        if x in arr:
            arr.remove(x)
        else:
            print("Element not found.")

    elif choice == 3:
        x = int(input("Enter number to search: "))
        if x in arr:
            print("Found at index", arr.index(x))
        else:
            print("Not Found")

    elif choice == 4:
        print("Array =", arr)

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")