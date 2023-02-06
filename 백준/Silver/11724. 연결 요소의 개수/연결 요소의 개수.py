import sys
input = sys.stdin.readline
N,M = map(int,input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1
cnt = 0
def bfs(V):
    queue = [V]
    visited[V] = 1
    while queue:
        V = queue.pop(0)
        for i in range(1,N+1):
            if (visited[i]==0 and matrix[V][i]==1):
                queue.append(i)
                visited[i] = 1
for i in range(1,N+1):
    if visited[i] == 0:
        cnt += 1
        bfs(i)
print(cnt)

    
