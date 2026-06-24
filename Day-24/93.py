#write a program to check string rotation.
s1=input("Enter first string:")
s2=input("Enter second string:")
if len(s1)==len(s2) and s2 in (s1+s1):
    print("String Rotation")
else:
    print("Not a String Rotation")
    