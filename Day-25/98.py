#write a program to find common characters in array.
str1=input("Enter first string:")
str2=input("Enter second string:")
common=set(str1) & set(str2)
print("Common Characters:","".join(common))


