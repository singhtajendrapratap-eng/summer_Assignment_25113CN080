#write a program to remove duplicate characters.
s= input("Enter a string:")
result=""
for ch in s:
    if ch not in result:
        result+=ch
print("After removing duplicates:",result)       
