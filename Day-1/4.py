# Write a program to count the number of digits in a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("The number of digits in the given number is:", count)