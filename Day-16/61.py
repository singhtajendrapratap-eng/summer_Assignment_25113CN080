#write a program to find missing number in array.
def find_missing_number(arr, n):

    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    missing_number = total_sum - arr_sum
    return missing_number
n = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
missing_number = find_missing_number(arr, n)
print("The missing number is:", missing_number)

