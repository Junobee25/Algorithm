import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y):
    visited[x][y] = 1
    if graph[x][y] == 1:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    dfs(nx,ny)
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0: break
    graph = []
    visited = [[0]*w for _ in range(h)]
    answer = 0
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    for x in range(h):
        for y in range(w):
            if visited[x][y] == 0  and graph[x][y] == 1:
                dfs(x,y)
                answer += 1
            else:
                continue
    print(answer)