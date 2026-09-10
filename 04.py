# Write a Python Program to Check Prime Number. 

import math

n = int(input('Enter a number: '))

if n>1:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print('Number is not prime.')
            break
        else:
            print('Number is prime.')
else:
    print('Number is not prime.')