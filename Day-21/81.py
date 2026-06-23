#write a program to find string length without strlen().
s=input("Enter a string=")
count=0
for ch in s:
    count+=1
print("Length=",count)