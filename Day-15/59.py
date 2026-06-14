#write a program to rotate array right.
def rotate_array_right(arr, d):
    d = d % len(arr)  # Handle cases where d is greater than array length
    return arr[-d:] + arr[:-d]
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
d = int(input("Enter the number of positions to rotate right: "))
rotated_array = rotate_array_right(array, d)
print("Array after right rotation:", rotated_array)



