#Write a program to check strong number.
def is_strong(num):
    sum_of_factorials = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        temp //= 10
    return sum_of_factorials == num
number = int(input("Enter a number to check if it is a strong number: "))
if is_strong(number):
    print(number, "is a strong number.")
else:
    print(number, "is not a strong number.")
    