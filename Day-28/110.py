#write a program to create bank account system.
balance = 0

while True:
    print("\n===== Bank Account System =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully.")

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    elif choice == 3:
        print("Current Balance =", balance)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")