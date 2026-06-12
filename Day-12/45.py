#write a program erite function for palindrome.
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")



                