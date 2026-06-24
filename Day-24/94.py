#write a program to compress a string.
s=input("Enter a string:")
compressed=""
count=1
for i in range(len(s)):
    if i<len(s)- 1 and s[i]==s[i+1]:
        count+=1
    else:
        compressed+=s[i]+str(count)
        count=1
print("Compressed string",compressed)
