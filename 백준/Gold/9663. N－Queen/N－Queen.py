N = int(input())
a = [False]*N
b = [False]*(2*N-1)
c = [False]*(2*N-1)
cnt = 0
def dfs(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):
            a[j] = True
            b[i+j] = True
            c[i-j+N-1] =True
            dfs(i+1)
            a[j] = False
            b[i+j] = False
            c[i-j+N-1] =False

dfs(0)
print(cnt)
