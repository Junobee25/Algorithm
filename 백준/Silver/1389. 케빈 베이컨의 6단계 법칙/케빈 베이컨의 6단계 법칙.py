# 한 정점에서 다른 정점까지의 거리의 합이 가장 작은 노드 구하기
# 노드가 여러개면 노드 번호가 작은 노드 구하기
n,m = map(int,input().split())

INF = int(1e9)

# 2차원 리스트 무한으로 초기화
graph = [[INF]*(n + 1) for _ in range(n+1)]

# 자기자신 0으로 초기화
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선 가중치 부여 (양방향 그래프)
for i in range(1,m+1):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플루이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈베이커리 값이 같으면 번호가 작은것 출력(정렬)         
result = []

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        cnt += graph[i][j]
    result.append((cnt,i))

result.sort()
print(result[0][1])


