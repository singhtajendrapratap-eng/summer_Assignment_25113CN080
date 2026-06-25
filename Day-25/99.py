#write a program to sort names alphabetically.
names=input("Enter names separated by space:").split()
names.sort()
print("Names in Alphabetical order:")
for name in names:
    print(name)
    