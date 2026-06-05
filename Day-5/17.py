#Write a program to check perfect number.
def is_perfect(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
number = int(input("Enter a number to check if it is a perfect number: "))
if is_perfect(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")


