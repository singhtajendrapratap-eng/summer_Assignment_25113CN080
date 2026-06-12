#write a program to write function for fibonacci.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence
number = int(input("Enter the number of Fibonacci terms: "))
result = fibonacci(number)
print(f"The first {number} terms of the Fibonacci sequence are: {result}")



            