#write a program to recursive fibonacci.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
number = int(input("Enter a number to find its Fibonacci: "))
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")




            