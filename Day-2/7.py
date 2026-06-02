#Write a program to find the product of the digits of a given number.
def product_of_digits(num):
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10
    return product      
number = int(input("Enter a number: "))
result = product_of_digits(number)
print("The product of the digits of", number, "is:", result)

