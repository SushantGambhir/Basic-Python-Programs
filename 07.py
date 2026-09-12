# Write a Python Program to Print the Fibonacci Sequence

def fibonacci(n):
    a,b=0,1

    terms = []

    for i in range(n):
        terms.append(a)
        a, b = b, a+b

    return terms

n = int(input('Enter number of terms: '))
res = fibonacci(n)

for i in res:
    print(i, end=' ')