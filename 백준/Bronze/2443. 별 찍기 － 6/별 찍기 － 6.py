N = int(input())
for i in range(N,0,-1):
    star = ''
    for k in range(i,N):
        star += ' '
    for j in range(2*i-1):
        star += '*'
    print(star)

    