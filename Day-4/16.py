#WRITE A PROGRAM TO PRINT ARMSTRONG NUMBERS IN A GIVEN RANGE.
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):    
    if is_armstrong(num):
        print(num)