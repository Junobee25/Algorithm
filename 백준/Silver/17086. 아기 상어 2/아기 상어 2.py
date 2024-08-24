import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()

dy = [-1,1,0,0,-1,-1,1,1]
dx = [0,0,-1,1,-1,1,-1,1]

result = 0

def bfs():
    while q:
        y,x = q.popleft()
        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            
            if not arr[ny][nx]:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny, nx))
                
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            q.append((i,j))
            
bfs()

for a in arr:
    result = max(max(a), result)
    
print(result - 1)