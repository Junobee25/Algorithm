import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

matrix = []
visited = [[False]*m for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for _ in range(n):
    k = list(map(int,input().rstrip().split()))
    matrix.append(k)

picture_cnt = 0

areas_list = []


def bfs(y,x):
    global picture_cnt
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    cnt = 0
    cnt += 1
    while q:
     cy,cx = q.pop()
     for k in range(4):
         ny = cy + dy[k]
         nx = cx + dx[k]
         if 0 <= ny < n and 0 <= nx < m:
             if visited[ny][nx] == False and matrix[ny][nx] == 1:
                cnt += 1
                visited[ny][nx] = True
                q.append((ny,nx))
    areas_list.append(cnt)
    picture_cnt += 1

             
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == False:
            bfs(i,j)

print(picture_cnt)

if len(areas_list) == 0:
    print(0)
else:
    print(max(areas_list))