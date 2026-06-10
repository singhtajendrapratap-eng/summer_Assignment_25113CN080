#write a program to print half pyramid pattern.
def half_pyramid(n):
    for i in range(1, n + 1):
        print("* " * i)
number = int(input("Enter the number of rows for the half pyramid: "))
half_pyramid(number)
        