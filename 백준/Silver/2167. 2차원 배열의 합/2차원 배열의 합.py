# 열 배열 탐색
n, m = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))

k = int(input())


for _ in range(k):
    b,a,y,x = map(int,input().split())
    result = 0
    for i in range(n):
        for j in range(m):
            if i < b - 1 or i > y -1 or j < a -1 or j > x - 1:
                continue
            else:
                result += matrix[i][j]

    print(result)

            
            