#Write a program to reverse a given number.
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num
number = int(input("Enter a number: "))
result = reverse_number(number)     
print("The reverse of", number, "is:", result)    