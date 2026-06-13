#write a program to count even and odd elements.
def count_even_odd(arr):
    even_count = odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
even_count, odd_count = count_even_odd(array)
print(f"Number of even elements: {even_count}")
print(f"Number of odd elements: {odd_count}")




                