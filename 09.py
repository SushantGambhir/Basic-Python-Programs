#  Write a Python Program to Find Armstrong Numbers in an Interval

def checkArmstrong(num):
    order = len(str(num))
    sum = 0

    temp = num
    while temp > 0:
        digit = temp%10
        sum+=digit**order
        temp//=10

    if sum==num:
        return True
    else:
        return False

start = int(input('Enter start: '))
end = int(input('Enter end: '))

armNums = []

for i in range(start, end+1):
    if(checkArmstrong(i)):
        armNums.append(i)

for i in armNums:
    print(i)