# 첫째줄 배추를 심은 배추밭의 가로길이 M
# 세로길이 N
# 배추가 심어져있는 위치의 개수 K
T = int(input())
for i in range(T):
    M,N,K = map(int,input().split())

    # 그다음 K줄 배추의 위치 X,Y가 주어진다.
    location = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    # 군수를 담을 리스트 생성
    result = [] 
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for i in range(K):
        X, Y = map(int,input().split())
        location[Y][X] = 1

    def dfs(y,x):
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if location[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    dfs(ny,nx)


    for i in range(N):
        for j in range(M):
            if location[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                each = 0
                dfs(i,j)
                result.append(each)
    print(len(result))