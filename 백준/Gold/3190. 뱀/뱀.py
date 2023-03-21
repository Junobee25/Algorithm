from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

matrix = [[0]*n for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

# 사과는 1로
for i in range(k):
    a, b = map(int,input().split())
    matrix[a-1][b-1] = 2

# 방향전환 정보 딕셔너리에 저장
v = int(input())
direction = dict()
q = deque()
q.append((0,0))

for i in range(v):
    a, b = input().split()
    a = int(a)
    direction[a] = b

y,x = 0,0
matrix[y][x] = 1
cnt = 0
direc = 0

def vector(turn):
    global direc
    if turn == 'L':
        direc = (direc - 1) % 4
    else:
        direc = (direc + 1) % 4

while True:
    cnt += 1
    y += dy[direc]
    x += dx[direc]

    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if matrix[y][x] == 2:
        matrix[y][x] = 1
        q.append((y,x))
        if cnt in direction:
            vector(direction[cnt])
    elif matrix[y][x] == 0:
        matrix[y][x] = 1
        q.append((y,x))
        ny,nx = q.popleft()
        matrix[ny][nx] = 0
        if cnt in direction:
            vector(direction[cnt])
    else:
        break
print(cnt)

