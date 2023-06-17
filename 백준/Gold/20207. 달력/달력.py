n = int(input())


calender = [0]*366

for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        calender[i] += 1


max_value = 0

width = 0

result = 0




for i in range(len(calender)):
    if calender[i] == 0:
        result += max_value * width
        max_value = 0
        width = 0

    if calender[i] != 0 :
        if calender[i] > max_value:
            max_value = calender[i]
        width += 1
    if i == len(calender) - 1:
        result += max_value*width

if 0 not in calender:
    print(width*max_value)
else:
    print(result)
