#write a program to create student record system.
students = []

while True:
    print("\n----- STUDENT RECORD SYSTEM -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Roll No: ")
        name = input("Name: ")
        marks = float(input("Marks: "))
        students.append([roll, name, marks])

    elif choice == 2:
        roll = input("Enter Roll No: ")
        found = False
        for s in students:
            if s[0] == roll:
                print("Roll:", s[0])
                print("Name:", s[1])
                print("Marks:", s[2])
                found = True
        if not found:
            print("Student not found.")

    elif choice == 3:
        print("\nStudent Records")
        for s in students:
            print(s)

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")