#write a program to merge arrays.
def merge_arrays(arr1, arr2):
    merged_array = arr1 + arr2
    return merged_array
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
merged_array = merge_arrays(array1, array2)
print(f"Merged array: {merged_array}")





                        