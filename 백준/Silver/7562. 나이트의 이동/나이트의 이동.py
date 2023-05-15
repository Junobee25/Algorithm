# 벡터로 설정된 값으로만 이동 가능
# 처음위치와 도착 위치가 제공
# 도착 위치로 가는 비용의 최소

# 루프가 돌면서 처음 찍힌 상황에만 cnt 증가 그리고 할당(큐 순서대로)
from collections import deque
T = int(input())



dy = [-2,-1,1,2,2,1,-1,-2]
dx = [1,2,2,1,-1,-2,-2,-1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    cnt = 0
    while q:
        y,x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False:
                q.append((ny,nx))
                cnt = 1
                # q에 append 요소를 기준으로 cnt가 더해져야 함 (중요)
                board[ny][nx] = board[y][x] + cnt
                visited[ny][nx] = True

for _ in range(T):
    n = int(input())

    start_yx = tuple(map(int,input().split()))
    goal_yx = tuple(map(int,input().split()))

    board = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    bfs(start_yx[0],start_yx[1])

    print(board[goal_yx[0]][goal_yx[1]])
