#  Write a Python program to solve a quadratic equation. 

import math

a = int(input('Enter coefficient of x^2: '))
b = int(input('Enter coefficient of x: '))
c = int(input('Enter the constant term: '))

disc = b*b - 4*a*c

if disc>0:
    r1 = (-b + math.sqrt(disc))/(2*a)
    r2 = (-b - math.sqrt(disc))/(2*a)
    print(f'The roots are: {r1} and {r2}')

elif disc==0:
    r = (-b + math.sqrt(disc))/2
    print(f'Single root: {r}')

else:
    print('No real roots')
