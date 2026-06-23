#write a program to reverse array.
def reverse_array(arr):
    return arr[::-1]
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

reversed_array = reverse_array(array)
print("Reversed array:", reversed_array)

        





