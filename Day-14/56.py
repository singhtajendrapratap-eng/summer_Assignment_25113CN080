#write a program to find duplicates in array.
def find_duplicates(arr):
    duplicates = set()
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
duplicates = find_duplicates(array)
if duplicates:
    print("Duplicate elements in the array are:", duplicates)
else:
    print("No duplicate elements found in the array.")



    