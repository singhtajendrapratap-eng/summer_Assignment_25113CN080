#write a program to check anagram strings.
s1=input("Enter first string:").replace(" ","")
s2=input("Enter second string:").replace(" ","")
if sorted(s1)==sorted(s2):
    print("Anagram Strings")
else:
    print("Not Anagram Strings")
        