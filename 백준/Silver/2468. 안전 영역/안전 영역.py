# [비의 양은 정해져 있진 않지만
# 생각을 해보면
# 영역이 나올 수 있는 경우의 수는
# 비가 안내렸을 때부터
# 최대 높이까지 내렸을 때까지이므로
# 모든 경우를 고려해준다고하자.]


# [비의양 : x(0) ~ 비의양 max(matrix[i][j])까지

# x >= matrix[i][j] 0번으로
# x < matrix[i][j] 1번으로 체크

# 위와 같이 설정한 행렬에서
# bfs를 돌면서
# 상하좌우가 1로 표시된 영역의 개수를 갱신 시킨다.

# max_result 보다 크다면
# max_result = 영역의 크기

# print(max_result)


# 위는 로직

# 구현만 잘해보자

# copy method
from copy import deepcopy
from collections import deque
n = int(input())

# 초기 영역 matrix
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

min_height = 0
max_height = 0


# 일단 높이 최대값 구하기
for i in range(n):
    for j in range(n):
        if matrix[i][j] >= max_height:
            max_height = matrix[i][j]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
max_result = 0
for k in range(max_height+1):
    copy_matrix = deepcopy(matrix)
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if copy_matrix[i][j] <= k:
                copy_matrix[i][j] = 0
            else:
                copy_matrix[i][j] = 1
    # bfs 로직 구현하기

    def bfs(y, x):
        global cnt
        global max_result
        q = deque()
        q.append((y, x))
        while q:
            ny, nx = q.popleft()
            for i in range(4):
                py = ny + dy[i]
                px = nx + dx[i]
                if 0 <= py < n and 0 <= px < n:
                    if copy_matrix[py][px] == 1 and visited[py][px] == False:
                        visited[py][px] = True
                        q.append((py, px))

        cnt += 1
        if cnt >= max_result:
            max_result = cnt
    for i in range(n):
        for j in range(n):
            if copy_matrix[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)

print(max_result)