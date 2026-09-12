#  Write a Python Program to Find the Sum of Natural Numbers. 

n = int(input('Enter a number: '))

sum = 0

for i in range(n+1):
    sum+=i

print(sum)