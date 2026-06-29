#write a program to create a menu driven string operation.
s = input("Enter a string: ")

while True:
    print("\n----- STRING OPERATIONS -----")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Reverse")
    print("4. Length")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(s.upper())

    elif choice == 2:
        print(s.lower())

    elif choice == 3:
        print(s[::-1])

    elif choice == 4:
        print("Length =", len(s))

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")