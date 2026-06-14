#write a program to find commoin elements.
def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    return common
number_of_elements1 = int(input("Enter the number of elements in the first list: "))
list1 = []
for i in range(number_of_elements1):
    element = int(input(f"Enter element {i + 1} for the first list: "))
    list1.append(element)
number_of_elements2 = int(input("Enter the number of elements in the second list: "))
list2 = []
for i in range(number_of_elements2):
    element = int(input(f"Enter element {i + 1} for the second list: "))
    list2.append(element)
common = common_elements(list1, list2)
print(f"Common elements between the two lists: {common}")




                