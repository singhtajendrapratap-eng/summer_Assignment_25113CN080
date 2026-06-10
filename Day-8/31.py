#write a program to print character triangle.
def character_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")
        print()
number = 5
character_triangle(number)

        