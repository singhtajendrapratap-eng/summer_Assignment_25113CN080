#write a program to print character pyramid.
def character_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")
        print()
number = 5
character_pyramid(number)

        