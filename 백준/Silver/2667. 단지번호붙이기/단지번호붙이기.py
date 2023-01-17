import sys
input = sys.stdin.readline
N = int(input())
# N*N map 생성
map = [list(map(int,input().strip())) for _ in range(N)]
# 방문리스트
visited = [[False]*N for _ in range(N)]
# 군안의 집의 갯수를 담을 result  , result의 길이는 군수
result = []
# 군안의 집의 갯수를 담을 전역변수
each = 0
# 4방향 for문이 돌때마다 한방향씩 탐색
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N: # N*N 범위 안이면
            if map[ny][nx] == 1 and visited[ny][nx] == False: # 집이있고 방문을 안했으면
                visited[ny][nx] = True # 방문처리
                dfs(ny,nx) # 재귀호출
# 이중포문으로 집이 있는 곳 찾기 처음으로 집이있다면 함수 호출하며 4방향으로 탐색
for i in range(N):  
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            each = 0
            dfs(i,j)
            result.append(each) # 스택에 저장된 each들 append 해주기
result.sort()
print(len(result))
for i in result:
    print(i)