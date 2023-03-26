# 문제 이해
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
# X로부터 출발하여 도달 할 수 있는 도시 중 최단 거리가 K인 모든 도시 번호
# 없으면 -1

# bfs탐색 중 queue에 원소가 들어갈 때마다 cnt += 1 result 리스트에도 원소 담기
# 만약에 k == cnt break걸고 result리스트에 있는 원소 오름차순으로 출력
from collections import deque
n, m, k, x = map(int,input().split())

matrix = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

# 노드까지의 거리를 저장해둘 리스트
dist = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    matrix[a].append(b)


def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    while q:
        node = q.popleft()
        visited[node] = True        
        for i in matrix[node]:
            if visited[i] == False:
                visited[i] = True
                dist[i] += dist[node] + 1
                q.append(i)

    if k in dist:
        for i in range(len(dist)):
            if dist[i] == k:
                print(i)
    else:
        print(-1)


bfs(x)