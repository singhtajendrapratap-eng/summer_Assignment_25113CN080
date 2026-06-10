#write a program to print reverse star pattern.
def reverse_star_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)
number = 5
reverse_star_pattern(number)

