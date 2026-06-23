#write a program to find first repeating charcter .
s=input("Enter a string:")
seen=set()
for ch in s:
    if ch in seen:
        print("First repeating character:",ch)
        break
    seen.add(ch)
else:
    print("No repeating character found")
    