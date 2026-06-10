#write a program to print repeated character pattern.
def repeated_character_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(64 + i), end=" ")
        print()
number = 5
repeated_character_pattern(number)
    