#write a program to count set bits in a number.
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
number = int(input("Enter a number to count its set bits: "))
result = count_set_bits(number)
print(f"The number of set bits in {number} is: {result}")

