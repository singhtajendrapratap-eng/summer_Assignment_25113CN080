#write a program to create mini employee mangement system.
employees = {}

while True:
    print("\n----- EMPLOYEE MANAGEMENT -----")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Delete Employee")
    print("4. Display Employees")
    print("5. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        empid = input("Employee ID: ")
        name = input("Employee Name: ")
        salary = float(input("Salary: "))
        employees[empid] = [name, salary]

    elif choice == 2:
        empid = input("Employee ID: ")
        if empid in employees:
            print(employees[empid])
        else:
            print("Employee not found.")

    elif choice == 3:
        empid = input("Employee ID: ")
        employees.pop(empid, None)

    elif choice == 4:
        for k, v in employees.items():
            print("ID:", k, "Name:", v[0], "Salary:", v[1])

    elif choice == 5:
        break

    else:
        print("Invalid Choice")