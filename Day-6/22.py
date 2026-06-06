#write a program to convert binary to decimal.
def binary_to_decimal(binary):
    decimal = 0
    binary_str = str(binary)
    length = len(binary_str)
    for i in range(length):
        bit = int(binary_str[length - 1 - i])
        decimal += bit * (2 ** i)
    return decimal
binary_number = input("Enter a binary number to convert to decimal: ")
result = binary_to_decimal(binary_number)
print(f"The decimal representation of {binary_number} is: {result}")




