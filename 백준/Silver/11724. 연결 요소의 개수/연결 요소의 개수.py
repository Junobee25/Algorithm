import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N,M = map(int,input().split())
matrix = [[] for _ in range(N)]
visited = [False] *(N)

for _ in range(M):
    a,b = map(int,input().split())
    matrix[a-1].append(b-1)
    matrix[b-1].append(a-1)

def dfs(V):
    visited[V] = True
    for i in matrix[V]:
        if visited[i] == False:
            visited[i]= True
            dfs(i)




cnt = 0
for i in range(N):
    if visited[i] == False:
        cnt +=1
        dfs(i)

print(cnt)
    
