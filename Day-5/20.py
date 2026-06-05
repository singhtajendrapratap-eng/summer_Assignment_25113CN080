#Write a program to find largest prime factor.
def largest_prime_factor(n):
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    if n > 2:
        max_prime = n
    return max_prime
number = int(input("Enter a number to find its largest prime factor: "))
result = largest_prime_factor(number)
if result != -1:
    print(f"The largest prime factor of {number} is: {result}")
else: 
    print(f"There are no prime factors for {number}.")

