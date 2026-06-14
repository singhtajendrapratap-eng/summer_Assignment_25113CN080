#write a program to find maximum frequency element.
def max_frequency_element(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    max_freq_elements = [num for num, freq in frequency.items() if freq == max_freq]
    return max_freq_elements, max_freq
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
max_freq_elements, max_freq = max_frequency_element(array)
print(f"Element(s) with the maximum frequency: {max_freq_elements} (Frequency: {max_freq})")




