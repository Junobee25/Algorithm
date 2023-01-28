N = int(input())

for i in range(2*N-1):
    res = ''
    if i > (2*N-1)//2:
        for x in range(i-N+1):
            res += ' '
        for y in range(2*N-1-i):
            res += '*'
    else:
        for j in range(N-1-i):
            res += ' '
        for k in range(i+1):
            res += '*'
    print(res)


# 공백 2개 별1
# 공백 1개 별2
# 공백 0개 별3
# 공백 1개 별2
# 공백 2개 별1