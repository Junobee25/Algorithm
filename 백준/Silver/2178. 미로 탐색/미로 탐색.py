from collections import deque
# 방향벡터 설정 (4방향 탐색)
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    while q:
       Node = q.popleft()
       y = Node[0]
       x = Node[1]
       for i in range(4):
           ny = y + dy[i]
           nx = x + dx[i]
           if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    arr[ny][nx] = arr[y][x] + 1
                    q.append([ny,nx])
    return arr[N-1][M-1]
                  
                    
# N*M 행렬 생성
N,M = map(int,input().split())
# 방문리스트
visited = [[False]*M for _ in range(N)]
# 조건에 맞게 탐색횟수 담을 변수 생성
cnt = 0
arr = []
for i in range(N):
    k = list(map(int,input()))
    arr.append(k)
        
print(bfs(0,0))