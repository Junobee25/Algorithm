N, M = map(int, input().split())
from collections import deque
queue = deque()
visited = [[0]*N for _ in range(M)]
# 일수
dis = [[0]*N for _ in range(M)]
# 방향벡터
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# 토마토 보드
board = []
for i in range(M):
    k = list(map(int, input().split()))
    board.append(k)
# bfs 탐색하면서 익은토마토 위치들을 queue에 담는다.
for i in range(M):
    for j in range(N):
        if board[i][j] == 1: # 익은 토마토 일때만 뻗어 나갈 수 있음
            queue.append((i,j)) # 위치튜플값을 저장

while queue:
    temp = queue.popleft()
    # 4방향 탐색
    for i in range(4):
        y = temp[0] + dy[i]
        x = temp[1] + dx[i]
    # 탐색의 기본 조건
        if 0<=y<M and 0<=x<N and board[y][x] == 0:
            board[y][x] = 1 # 익었다
            dis[y][x] = dis[temp[0]][temp[1]] + 1 # temp라고 해준이유는 익은토마토에서 비롯됬기 때문
            queue.append((y,x)) 
# 탐색이 끝나고 익지않은 0 번이 있을 때 플래그를 0으로 바꿔줌
flag = 1
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            flag = 0
result = 0
# 0번이없을때 최댓값 찾기
if flag == 1:
    for i in range(M):
        for j in range(N):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
# 0번이있으면 -1
else:
    print(-1)