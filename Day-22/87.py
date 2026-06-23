#write a program to character frequency.
s=input("Enter a string:")
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for key, value in freq.items():
    print(key,":",value)