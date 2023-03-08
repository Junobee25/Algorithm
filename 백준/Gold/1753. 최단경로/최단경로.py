import heapq
import sys
input = sys.stdin.readline
INF = 10**9
v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v + 1)
# 노드 간선 가중치 정보
for _ in range(e):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않을 동안
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

for result in distance[1:]:
    print(result if result != INF else "INF")