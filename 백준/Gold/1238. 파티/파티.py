import heapq

n,m,x = map(int,input().split())

INF = int(1e9)
# 1번 노드부터 n번노드까지 그래프 인접리스트
graph = [[] for _ in range(n+1)]

# n2logn으로 풀기휘애 2차원 거리테이블
# => 출발 노드부터 모든 거리 계산 해야함
# 플로이드는 시간초과 나기때문에
# heap djik로 구현
distance = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            distance[i][j] = 0

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


def dijkstra(turn,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[turn][start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[turn][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[turn][i[0]]:
                distance[turn][i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 1번노드부터 추발해서 거리테이블 갱신하기
for i in range(1,n+1):
    dijkstra(i,i)

max_val = -99
for i in range(1,len(distance)):
    k = distance[i][x] + distance[x][i]
    if k > max_val:
        max_val = k
print(max_val)