# 무방향 그래프에서 s -> t로 도달 하는 최단 거리
import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int,input().split())
INF = int(1e9)
distance = [INF]*(n+1)
visited = [False]*(n+1)

def djikstra(start):
    q = []
    distance[start] = 0
    visited[start] = True
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
djikstra(s)
print(distance[t])