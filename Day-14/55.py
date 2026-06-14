#write a program to second largest element.
def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second if second != float('-inf') else None
numbers = [10, 20, 5, 30, 15]
result = second_largest(numbers)
if result is not None:
    print(f"The second largest element is: {result}")
else:
    print("There is no second largest element.")



            