#write a program to find x^n without pow().
def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n
    result = 1
    for _ in range(n):
        result *= x
    return result
base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (n): "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")

