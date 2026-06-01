# Write a program to find the factorial of a given number
num = int(input("Enter a number: "))    
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is:", factorial)