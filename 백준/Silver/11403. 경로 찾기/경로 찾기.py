# 플루이드 워셜알고리즘
# 모든 노드에서 모든노드까지의 경로를 찾는다.
# 경로가 없으면 0표시 경로가 있으면 1표시

n = int(input())

INF = int(1e9)
# 인접행렬 입력값
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))


# 경로리스트
graph = [[INF]*(n+1) for _ in range(n+1)]


# 경로있으면 체크 가중치 없으므로 1로 갱신(단방향)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i+1][j+1] = 1

# 자기자신 = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = INF

# 플루이드 워셜 알고리즘 수행
# 모든노드에서 모든노드까지의 최단경로
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

answer = []
for i in range(1,n+1):
    arr = []
    for j in range(1,n+1):
        if graph[i][j] == INF:
            arr.append(0)
        else:
            arr.append(1)
    answer.append(arr)

# 결과 출력
for i in range(n):
    for j in range(n):
        print(answer[i][j],end=" ")
    print()