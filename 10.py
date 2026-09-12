#  Write a Python Program to Find the Sum of Natural Numbers. 

n = int(input('Enter a number: '))

# Brute force O(n) solution

# sum = 0

# for i in range(n+1):
#     sum+=i

# print(sum)

# Optimal O(1) solution

sum = n*(n+1)//2
print(sum)