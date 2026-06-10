#write a program to print star pyramid .
def star_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " *  (2 * i - 1))
number = 5
star_pyramid(number)
