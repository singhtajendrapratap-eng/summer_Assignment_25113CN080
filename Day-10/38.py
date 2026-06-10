#write a program to print reverse pyramid .
def reverse_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " *  (2 * i - 1))
number = 5
reverse_pyramid(number)
    