#WRITE A PROGRAM TO FIND NTH FIBONACCI TERM.
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
num = int(input("Enter the term number to find in the Fibonacci series: "))
result = fibonacci(num)
print(f"The {num}th term in the Fibonacci series is: {result}")