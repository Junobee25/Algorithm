def solution(n):
    triangle = [[0]*n for _ in range(n)]
    y,x = -1,0
    result = []
    number = 1
    for i in range(1,n+1):
        for j in range(n+1-i):
            if i % 3 == 1:
                y += 1
                triangle[y][x] = number
            elif i % 3 == 2:
                x += 1
                triangle[y][x] = number
            else:
                y -= 1
                x -= 1
                triangle[y][x] = number

            number += 1

    for i in range(n):
        for j in range(n):
            if triangle[i][j] != 0:
                result.append(triangle[i][j])
    return result