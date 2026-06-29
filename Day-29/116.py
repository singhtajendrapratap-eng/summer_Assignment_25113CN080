#write a program to create inventory management system.
inventory = {}

while True:
    print("\n----- INVENTORY MANAGEMENT -----")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Display Inventory")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Product Name: ")
        qty = int(input("Quantity: "))
        inventory[name] = qty

    elif choice == 2:
        name = input("Product Name: ")
        if name in inventory:
            inventory[name] = int(input("New Quantity: "))
        else:
            print("Product not found.")

    elif choice == 3:
        name = input("Product Name: ")
        inventory.pop(name, None)

    elif choice == 4:
        print("\nInventory:")
        for item, qty in inventory.items():
            print(item, ":", qty)

    elif choice == 5:
        print("Program Closed.")
        break

    else:
        print("Invalid Choice")