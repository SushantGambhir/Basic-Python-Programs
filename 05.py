#  Write a Python Program to Print all Prime Numbers in a specified interval

import math

n = int(input('Tell the number till where you want the prime numbers: '))

primes = []

if n>1:
    for i in range(1,n+1):
        isPrime=True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                isPrime=False
                break
        if(isPrime):
            primes.append(i)

for itr in primes:
    print(itr)