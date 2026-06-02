# Write a program to find the sum of the digits of a given number.
def sum_of_digits(num):     
    sum = 0     
    while(num > 0):     
        digit = num % 10     
        sum += digit     
        num //= 10     
    return sum
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("The sum of the digits of", number, "is:", result)    
