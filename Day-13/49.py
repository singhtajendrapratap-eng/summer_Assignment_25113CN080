#write a program to input and display array.
def input_array(n):
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    return arr
def display_array(arr):
    print("The elements in the array are:")
    for element in arr:
        print(element, end=" ")
number_of_elements = int(input("Enter the number of elements in the array: "))
array = input_array(number_of_elements)
display_array(array)



                