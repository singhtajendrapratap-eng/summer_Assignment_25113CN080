#write a program to create quiz application.
score = 0

print("Python Quiz")

q1 = input("1. Who developed Python?\n(a) James Gosling\n(b) Guido van Rossum\n(c) Dennis Ritchie\nAnswer: ")
if q1.lower() == "b":
    score += 1

q2 = input("\n2. Which keyword is used to define a function?\n(a) function\n(b) define\n(c) def\nAnswer: ")
if q2.lower() == "c":
    score += 1

q3 = input("\n3. Which data type is mutable?\n(a) List\n(b) Tuple\n(c) String\nAnswer: ")
if q3.lower() == "a":
    score += 1

print("\nYour Score =", score, "/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good Job!")
else:
    print("Keep Practicing!")