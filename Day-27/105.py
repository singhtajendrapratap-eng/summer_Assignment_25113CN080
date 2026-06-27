#write a program to create student record management system.
students = {}

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        students[roll] = {"Name": name, "Course": course}
        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            for roll, data in students.items():
                print(roll, data)
        else:
            print("No Records Found.")

    elif choice == "3":
        roll = input("Enter Roll No: ")
        if roll in students:
            print(students[roll])
        else:
            print("Student Not Found.")

    elif choice == "4":
        roll = input("Enter Roll No: ")
        if roll in students:
            del students[roll]
            print("Record Deleted.")
        else:
            print("Student Not Found.")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")