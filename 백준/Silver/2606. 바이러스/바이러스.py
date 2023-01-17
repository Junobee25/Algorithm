N = int(input()) # 정점의 갯수
M = int(input()) # 간선의 갯수 -> 트리 만들기

matrix = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    visited[V] = 1
    for i in range(1,N+1):
        if visited[i] ==0 and matrix[V][i] == 1:
            dfs(i)

dfs(1)
print(visited.count(1)-1)