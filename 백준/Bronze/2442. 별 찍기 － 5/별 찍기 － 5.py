T = int(input())
for i in range(1,T+1):
    star = ''
    for j in range(T-i):
        star += ' '
    for k in range(2*i-1):
        star += '*'
    print(star)
