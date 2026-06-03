#WRITE A PROGRAM TO FIND LCM OF TWO NUMBERS.
from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)     
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is:", result)



