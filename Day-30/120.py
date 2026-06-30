#write a program to create mini project by using string , arrays and functions.
students = {}

def add_student():
    roll = input("Roll Number: ")
    name = input("Name: ")
    marks = float(input("Marks: "))
    students[roll] = [name, marks]
    print("Student Added.")

def search_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Name:", students[roll][0])
        print("Marks:", students[roll][1])
    else:
        print("Student Not Found")

def update_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        students[roll][0] = input("New Name: ")
        students[roll][1] = float(input("New Marks: "))
        print("Updated Successfully")
    else:
        print("Student Not Found")

def delete_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        del students[roll]
        print("Deleted Successfully")
    else:
        print("Student Not Found")

def display_students():
    if not students:
        print("No Records Found")
    else:
        print("\nStudent Records")
        for roll, data in students.items():
            print("Roll:", roll,
                  "Name:", data[0],
                  "Marks:", data[1])

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        display_students()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")