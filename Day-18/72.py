#write a program to sort array in descending order.
def descending_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = descending_sort(arr)
print("Sorted array in descending order is:", sorted_arr)




                