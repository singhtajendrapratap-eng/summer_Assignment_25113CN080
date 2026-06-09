#write a program to recursive reverse number.
def reverse_number(n):
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_number(n // 10)
number = int(input("Enter a number to reverse: "))
result = reverse_number(number)
print(f"The reverse of {number} is: {result}")              
