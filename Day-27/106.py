#write a program to create employee management system.
employees = {}

while True:
    print("\n--- Employee Management ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        employees[empid] = {"Name": name, "Department": dept}
        print("Employee Added!")

    elif ch == "2":
        if employees:
            for empid, data in employees.items():
                print(empid, data)
        else:
            print("No Employees.")

    elif ch == "3":
        empid = input("Enter Employee ID: ")
        if empid in employees:
            print(employees[empid])
        else:
            print("Employee Not Found.")

    elif ch == "4":
        empid = input("Enter Employee ID: ")
        if empid in employees:
            del employees[empid]
            print("Employee Deleted.")
        else:
            print("Employee Not Found.")

    elif ch == "5":
        break

    else:
        print("Invalid Choice")