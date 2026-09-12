# Write a Python Program to Display the Multiplication Table.

def printTable(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

n = int(input('Enter a number: '))
printTable(n)