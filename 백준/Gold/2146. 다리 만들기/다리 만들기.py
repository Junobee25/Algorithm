import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
cnt = 1
result = 999999
# 먼저는 섬을 구분하기
def divide_island(i,j):
    global cnt
    q = deque()
    q.append([i,j])
    visited[i][j] = True
    matrix[i][j] = cnt   # 섬이 연결되는 동안 cnt로 구분

    while q:
        y,x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                matrix[ny][nx] = cnt
                q.append([ny,nx])
# 바다를 지나면서 가장 짧은 거리를 구하기
def short_dist(z):
    global result
    dist = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == z:
                q.append([i,j])
                dist[i][j] = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 갈 수 없는 곳이면 continue
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if matrix[ny][nx] > 0 and matrix[ny][nx] != z:
                result = min(result,dist[y][x])
                return
            # 바다를 만나면 dist를 1씩 늘림
            if matrix[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny,nx])

for i in range(n):
    for j in range(n):
        if not visited[i][j] and matrix[i][j] == 1:
            divide_island(i,j)
            cnt += 1

for i in range(1,cnt):
    short_dist(i)

print(result)