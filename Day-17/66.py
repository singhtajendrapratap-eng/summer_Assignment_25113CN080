#write a program to union of arrays.
def union_of_arrays(arr1, arr2):
    union_array = list(set(arr1) | set(arr2))
    return union_array
number_of_elements1 = int(input("Enter the number of elements in the first array: "))
array1 = []
for i in range(number_of_elements1):
    element = int(input(f"Enter element {i + 1} for the first array: "))
    array1.append(element)
number_of_elements2 = int(input("Enter the number of elements in the second array: "))
array2 = []
for i in range(number_of_elements2):
    element = int(input(f"Enter element {i + 1} for the second array: "))
    array2.append(element)
union_array = union_of_arrays(array1, array2)
print(f"Union of the two arrays: {union_array}")




                