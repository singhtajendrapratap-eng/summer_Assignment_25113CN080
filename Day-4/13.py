#wRITE A PROGRAM TO GENERATE FIBONACCI SERIES.
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
num = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci(num)
print("Fibonacci series:")
print(result)
