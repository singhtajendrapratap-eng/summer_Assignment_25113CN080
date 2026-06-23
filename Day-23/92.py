#write a program to find maximum frequency occuring character.
s=input("Enter a string:")
max_char=s[0]
max_count=s.count(max_char)
for ch in s:
    if s.count(ch)>max_count:
        max_count=s.count(ch)
        max_char=ch
print("Maximum occuring character:",max_char)
print("Frequency:",max_count)  
      