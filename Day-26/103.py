#write a program to create atm simulation.
balance = 10000
pin = "1234"

user_pin = input("Enter ATM PIN: ")

if user_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance =", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Amount Deposited Successfully.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful.")
            else:
                print("Insufficient Balance.")

        elif choice == 4:
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid Choice.")
else:
    print("Incorrect PIN.")