def dfs(L,sum):
    global res
    if L == N+1:
        if sum>res:
            res = sum
    else:
        if L+day[L]<=N+1:
            dfs(L+day[L],sum+money[L])
        dfs(L+1,sum)


N = int(input())
day = [0]
money = [0]
res = -21740000
for i in range(N):
    a,b = map(int,input().split())
    day.append(a)
    money.append(b)
dfs(1,0)
print(res)
    
