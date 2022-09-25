a = input().split(' ')
sum1 = 0
for i in range(0,len(a)):
    sum1 += int(a[i])**2
print(sum1%10)