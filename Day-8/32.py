#write a program to print repeated number pattern.
def repeated_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()
number = 5
repeated_number_pattern(number)

        
