from collections import deque
m,n,k = map(int,input().split())

matrix = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(m):
        for j in range(n):
            if (x1 <= j <= x2-1) and (y1 <= i <= y2-1):
                matrix[i][j] = 1


areas_cnt = 0
areas = []
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    global areas_cnt
    global areas
    q = deque()
    q.append((y,x))
    cnt = 0
    cnt += 1
    visited[y][x] = True
    while q:
       cy,cx = q.pop()
       for k in range(4):
           ny = cy + dy[k]
           nx = cx + dx[k]
           if 0 <= ny < m and 0 <= nx < n and visited[ny][nx] == False and matrix[ny][nx] == 0:
               cnt += 1
               visited[ny][nx] = True
               q.append((ny,nx))
    areas_cnt += 1
    areas.append(cnt)
               
           





for i in range(m):
    for j in range(n):
        if visited[i][j] == False and matrix[i][j] == 0:
            bfs(i,j)

print(areas_cnt)
areas.sort()
for i in areas:
    print(i, end = " ")