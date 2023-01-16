T = int(input())
for i in range(T,0,-1):
    star = ''
    for j in range(T-i):
        star += ' '
    for k in range(2*i-1):
        star += '*'
    print(star)
for i in range(2,T+1):
    star = ''
    for j in range(T-i):
        star += ' '
    for k in range(2*i-1):
        star += '*'
    print(star)
