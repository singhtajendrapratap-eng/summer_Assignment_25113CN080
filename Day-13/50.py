# write a program to find sum and average of array.
def sum_and_average(arr):
    total_sum = sum(arr)
    average = total_sum / len(arr) if arr else 0
    return total_sum, average
numbers = [10, 20, 30, 40, 50]
total_sum, average = sum_and_average(numbers)
print(f"Sum: {total_sum}, Average: {average}")



                