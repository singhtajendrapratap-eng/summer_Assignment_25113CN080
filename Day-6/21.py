#write a program to convert decimal to binary.
def decimal_to_binary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary
number = int(input("Enter a decimal number to convert to binary: "))
result = decimal_to_binary(number)  
print(f"The binary representation of {number} is: {result}")




