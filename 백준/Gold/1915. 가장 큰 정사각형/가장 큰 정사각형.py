n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(input()))



# r자 채워주기
matrix.insert(0,[0 for _ in range(m+1)])

for i in range(1,n+1):
    matrix[i].insert(0,0)


# 최솟값 + 1으로 갱신
for i in range(1,n+1):
    for j in range(1,m+1):
        if int(matrix[i][j]) != 0:
            matrix[i][j] = min(int(matrix[i-1][j-1]),int(matrix[i-1][j]),int(matrix[i][j-1])) + 1
        else:
            matrix[i][j] = 0

# 넓이는 제곱
max_area = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if (matrix[i][j])**2 > max_area:
            max_area = matrix[i][j]**2
print(max_area)