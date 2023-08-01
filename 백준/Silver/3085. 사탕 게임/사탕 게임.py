n = int(input())

arr = []

for _ in range(n):
    k = list(input())
    arr.append(k)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

max_val = 0 # 먹을 수 있는 최대값


def change_idx(y,x,ny,nx): # 인접한 두 사탕 위치 바꿔주는 함수
    arr[y][x],arr[ny][nx] = arr[ny][nx],arr[y][x]

def row_check():
    global max_val
    for a in range(n):
        cnt = 1
        for b in range(1,n):
            if arr[a][b-1] == arr[a][b]:
                cnt += 1
            if arr[a][b-1] != arr[a][b]:
                if max_val < cnt:
                    max_val = cnt
                cnt = 1
            if b == n-1:
                if max_val < cnt:
                    max_val = cnt           



def col_check():
    global max_val
    for a in range(n):
        cnt = 1
        for b in range(1,n):
            if arr[b-1][a] == arr[b][a]:
                cnt += 1
            if arr[b-1][a] != arr[b][a]:
                if max_val < cnt:
                    max_val = cnt
                cnt = 1                
            if b == n-1:
                if max_val < cnt:
                    max_val = cnt                  
            
    
for i in range(n):
    for j in range(n):
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if arr[i][j] != arr[ny][nx]:
                    change_idx(i,j,ny,nx)
                    ## 행 열 최댓값 갱신하는 로직
                    row_check()
                    col_check()
                    change_idx(i,j,ny,nx)
                    ## 원상복귀


print(max_val)