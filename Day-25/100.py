#write a program to sort words by length .
words=input("Enter words separated by space:").split()
words.sort(key=len)
print("Words Sorted by length:")
for word in words:
    print(word)
    