n = int(input()) # n * n 행렬
cmd = input() # 문자열 명령

arr = [['' for _ in range(n)] for _ in range(n)]

# 초기 위치 좌표
y,x = 0,0

for c in cmd:
    if c == 'D':
        y += 1
        if (y >= n or y < 0) or (x >= n or x < 0):
            y -= 1
        else:
            arr[y-1][x] += c
            arr[y][x] += c
    elif c == 'U':
        y -= 1
        if (y >= n or y < 0) or (x >= n or x < 0):
            y += 1
        else:

            arr[y+1][x] += c
            arr[y][x] += c
       
    elif c == 'R':
        x += 1
        if (y >= n or y < 0) or (x >= n or x < 0):
            x -= 1
        else:
            arr[y][x-1] += c
            arr[y][x] += c

    elif c == 'L':
        x -= 1
        if (y >= n or y < 0) or (x >= n or x < 0):
            x += 1
        else:
            arr[y][x+1] += c
            arr[y][x] += c
for i in range(n):
    for j in range(n):
        if ('U' in arr[i][j] and 'R' in arr[i][j]) or ('U' in arr[i][j] and 'L' in arr[i][j]):
            arr[i][j] = '+'
        if ('D' in arr[i][j] and 'R' in arr[i][j]) or ('D' in arr[i][j] and 'L' in arr[i][j]):
            arr[i][j] = '+'
        if ('D' in arr[i][j] and 'R' not in arr[i][j] and 'L' not in arr[i][j]):
            arr[i][j] = '|'
        if ('U' in arr[i][j] and 'R' not in arr[i][j] and 'L' not in arr[i][j]):
            arr[i][j] = '|'
        if ('R' in arr[i][j] and 'U' not in arr[i][j] and 'D' not in arr[i][j]):
            arr[i][j] = '-'
        if ('L' in arr[i][j] and 'U' not in arr[i][j] and 'D' not in arr[i][j]):
            arr[i][j] = '-' 
        if arr[i][j] == '':
            arr[i][j] = '.'


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = "")
    print()     
