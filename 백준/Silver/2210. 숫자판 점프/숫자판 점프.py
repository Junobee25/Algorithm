def dfs(y, x, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0 ,-1]
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0 <= ny < 5 and 0 <= nx < 5:
            dfs(ny, nx, number + matrix[ny][nx])
            
            
matrix = [list(map(str, input().split())) for _ in range(5)]            
            
result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])
        
print(len(result))