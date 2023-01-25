import sys
input= sys.stdin.readline
from collections import deque
dy = [1,0,-1,0]
dx = [0,1,0,-1]
N = int(input())
arr = []
for i in range(N):
    k = list(map(str,input().rstrip()))
    arr.append(k)
visited = [[False]*N for _ in range(N)]

def bfs(y,x,color):
    q = deque()
    q.append([y,x])
    while q:
        Node = q.popleft()
        y = Node[0]
        x = Node[1]
        if visited[y][x] == False:
            visited[y][x] = True
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<N and 0<=nx<N:
                    if arr[ny][nx] == color:
                        q.append([ny,nx])

# 색약 x
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            color = arr[i][j]
            bfs(i,j,color)
            cnt += 1
# 색약
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            color = arr[i][j]
            bfs(i,j,color)
            cnt_2 += 1
print(cnt,cnt_2)

