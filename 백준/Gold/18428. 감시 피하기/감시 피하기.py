from itertools import combinations
import copy

n = int(input())

matrix = []

for i in range(n):
    k = list(input().split())
    matrix.append(k)

com = [(y,x) for x in range(n) for y in range(n) if matrix[y][x] == 'X']
combi = list(combinations(com,3))

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(y,x,matrix):
    visited = [[False]*n for _ in range(n)]
    stack = []
    stack.append((y,x))

    while stack:
        y,x = stack.pop()
        for i in range(4):
            for j in range(1,n+1):
                ny = y + dy[i]*j
                nx = x + dx[i]*j
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if matrix[ny][nx] == 'O':
                    break
                if matrix[ny][nx] == 'S':
                    return False 
    return True

for c in combi:

    set_map = copy.deepcopy(matrix)
    set_map[c[0][0]][c[0][1]] = 'O'
    set_map[c[1][0]][c[1][1]] = 'O'
    set_map[c[2][0]][c[2][1]] = 'O'

    answer = 'YES'

    for y in range(n):
        for x in range(n):
            if set_map[y][x] == 'T':
                if not dfs(y,x,set_map):
                    answer = 'NO'
        if answer == 'NO':
            break

    if answer == 'YES':
        break
print(answer)