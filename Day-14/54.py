#write a program to frequency of an element.
def frequency_of_element(arr, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
element_to_count = int(input("Enter the element to find its frequency: "))
frequency = frequency_of_element(array, element_to_count)
print(f"The frequency of {element_to_count} is: {frequency}")



