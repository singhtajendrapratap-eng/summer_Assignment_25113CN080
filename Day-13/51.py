#write a program to find largest and smallest element.
def find_largest_and_smallest(arr):
    if not arr:
        return None, None
    largest = smallest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest
numbers = [10, 20, 5, 30, 15]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest: {largest}, Smallest: {smallest}")


        