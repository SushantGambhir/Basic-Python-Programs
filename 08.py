#  Write a Python Program to Check Armstrong Number. 

def checkArmstrong(num):
    order = len(str(num))
    sum = 0

    temp = num
    while temp > 0:
        digit = temp%10
        sum+=digit**order
        temp//=10

    if sum==num:
        print('Number is Armstrong')
    else:
        print('Not Armstrong')

num = int(input('Enter a number: '))
checkArmstrong(num)