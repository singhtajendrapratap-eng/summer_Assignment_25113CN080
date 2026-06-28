#write a program to create ticket booking system.
total_seats = 10
booked = 0

while True:
    print("\n===== Ticket Booking System =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Available Seats")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if booked < total_seats:
            name = input("Enter passenger name: ")
            booked += 1
            print("Ticket booked successfully for", name)
        else:
            print("No seats available.")

    elif choice == 2:
        if booked > 0:
            name = input("Enter passenger name: ")
            booked -= 1
            print("Ticket cancelled for", name)
        else:
            print("No booked tickets.")

    elif choice == 3:
        print("Available Seats =", total_seats - booked)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")