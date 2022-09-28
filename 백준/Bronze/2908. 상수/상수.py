a = input().split(' ')
temp1 = a[0][0]
temp2 = a[0][2]
temp3 = a[1][0]
temp4 = a[1][2]
num1 = temp2+a[0][1]+temp1
num2 = temp4+a[1][1]+temp3

if num1>num2:
    print(num1)
elif num1<num2:
    print(num2)