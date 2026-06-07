#write a program to recursive reverse number.
def reverse_number(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_number = n // 10
        return last_digit * (10 ** len(str(remaining_number))) + reverse_number(remaining_number)
number = int(input("Enter a number to reverse: "))
result = reverse_number(number)
print(f"The reverse of {number} is: {result}")





                        