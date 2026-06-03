#Write a program to print prime number in a range.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Prime numbers in the range", start, "to", end, "are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
        