def DFS(L,s,plus):
    global cnt
    if L == K:
        if plus%number == 0 :
            cnt += 1
    else:
        for i in range(s,N):
            DFS(L+1,i+1,plus+arr[i])

N,K = map(int,input().split())
arr = list(map(int,input().split()))
number = int(input())
cnt = 0
res = [0] * (K+1)
DFS(0,0,0)
print(cnt)