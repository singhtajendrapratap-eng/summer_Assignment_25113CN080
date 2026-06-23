#write a program to remove duplicates from array.
def remove_duplicates(arr):
    unique_elements = list(set(arr))
    return unique_elements
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
unique_array = remove_duplicates(array)
print(f"Array after removing duplicates: {unique_array}")


