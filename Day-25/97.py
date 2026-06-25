#write a program to merge two sorted arrays.
arr1=list(map(int,input("Enter first sorted array:").split()))
arr2=list(map(int,input("Enter second sorted array:").split()))
merged=sorted(arr1+arr2)
print("Merged Array:",merged)
