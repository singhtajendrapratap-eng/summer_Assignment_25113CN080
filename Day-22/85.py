#write a program to check palindrome string.
s=input("Enter a string:")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    