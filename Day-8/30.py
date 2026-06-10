#write a program to print number triangle .
def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
number = 5
number_triangle(number)


