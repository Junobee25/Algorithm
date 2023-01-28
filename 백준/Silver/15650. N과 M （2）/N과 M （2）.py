def DFS(L):
    if L == M:
        if (all(res[k] < res[k+1] for k in range(L-1))) or (M==1):
            for j in range(M):
                print(res[j],end=" ")
            print()
        
    else:
        for i in range(1,N+1):
            if visited[i] == 0:
                visited[i] = 1
                res[L] = i
                DFS(L+1)
                visited[i] = 0
                
        
N,M = map(int,input().split())
visited = [0]*(N+1)
res = [0]*N
DFS(0)