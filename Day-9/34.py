#write a program to print reverse number triangle.
def reverse_number_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
number = 5
reverse_number_triangle(number)
