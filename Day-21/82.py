#write a program to to reverse a string.
s=input("Enter a string=")
rev=""
for ch in s:
    rev=ch+rev
print("Reversed string=",rev)