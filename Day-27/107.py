#write a program to create a salary management system.
employees = {}

while True:
    print("\n--- Salary Management System ---")
    print("1. Add Employee Salary")
    print("2. View Salary")
    print("3. Update Salary")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        hra = basic * 0.20
        da = basic * 0.10
        total = basic + hra + da
        employees[name] = total
        print("Salary Added Successfully!")

    elif choice == "2":
        for name, salary in employees.items():
            print(name, ":", salary)

    elif choice == "3":
        name = input("Enter Employee Name: ")
        if name in employees:
            basic = float(input("Enter New Basic Salary: "))
            hra = basic * 0.20
            da = basic * 0.10
            employees[name] = basic + hra + da
            print("Salary Updated.")
        else:
            print("Employee Not Found.")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")