# 비교 해야할 배열이 주어짐
# 값을 찾아야 할 배열 주어짐
# 정답을 기록할 배열 만들어야 함

# 구체화
# 모든 지뢰를 정답배열에 심어줄 함수 만들기

# 비교는 이중 포문으로 8방향 탐색

n = int(input())

boom_arr = []
open_arr = []
result = [['.']*n for _ in range(n)]

for i in range(n*2):
    if i < n:
        boom_arr.append(list(input()))
    else:
        open_arr.append(list(input()))

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
boom_idx = []

def boom():
    global result
    for i in boom_idx:
        result[i[0]][i[1]] = '*'

for i in range(n):
    for j in range(n):
        if boom_arr[i][j] == '*':
            boom_idx.append((i,j))


for y in range(n):
    for x in range(n):
        if open_arr[y][x] == 'x':
            if boom_arr[y][x] != '*':
                cnt = 0
                for k in range(8):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0<=ny<n and 0<=nx<n:
                        if boom_arr[ny][nx] == '*':
                            cnt += 1
                result[y][x] = cnt
            else:
                boom()
for i in range(n):
    for j in range(n):
        print(result[i][j], end = "")
    print()



