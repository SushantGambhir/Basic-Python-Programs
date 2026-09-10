# Write a Python Program to Check Prime Number. 

import math

n = int(input('Enter a number: '))

isPrime = True

if n>1:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            isPrime=False
            break

if(isPrime):
    print('Prime')
else:
    print('Non Prime')