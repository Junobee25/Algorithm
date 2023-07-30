a = input().split(':')
b = input().split(':')
for i in range(len(a)):
    a[i] = int(a[i])
    b[i] = int(b[i])
if a == b:
    print('24:00:00')
    exit()
s = 0
m = 0
h = 0
if a[2] > b[2]:
    a[1] += 1
    if a[1] == 60:
        a[1] = 0
        a[0] += 1
        if a[0] == 24:
            a[0] = 0
    s = 60 - a[2] + b[2]
elif a[2] <= b[2]:
    s = b[2] - a[2]

if a[1] > b[1]:
    a[0] += 1
    if a[0] == 24:
        a[0] = 0
    m = 60 - a[1] + b[1]
elif a[1] <= b[1]:
    m = b[1] - a[1]

if a[0] > b[0]:
    h = 24 - a[0] + b[0]
elif a[0] <= b[0]:
    h = b[0] - a[0]


h = str(h)
m = str(m)
s = str(s)

if len(h) == 1:
    h = '0' + h
if len(m) == 1:
    m = '0' + m
if len(s) == 1:
    s = '0' + s

print(h+':'+m+':'+s)
