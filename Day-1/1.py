# Write a program to calculate the sum of first N natural numbers
N = int(input("Enter the value of N:"))
sum=0
for i in range(1,N+1):
    sum=sum+i
print("The sum of first",N,"natural numbers is:",sum)    