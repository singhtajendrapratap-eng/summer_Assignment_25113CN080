#write a program to find pair with given sum.
def find_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
number_of_elements = int(input("Enter the number of elements in the array: "))
array = []
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
target_sum = int(input("Enter the target sum: "))
pair = find_pair_with_sum(array, target_sum)
if pair:
    print(f"Pair found: {pair[0]} and {pair[1]}")
else:
    print("No pair found with the given sum.")




                    