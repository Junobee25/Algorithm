T = int(input())  # 격자판 크기
arr = [list(map(int,input().split())) for _ in range(T)]  # 이차원 배열의 격자판 배열 생성

arr.insert(0,[0]*(T+2))  # 0으로 둘러싸기 
arr.append([0]*(T+2))

for i in range(T):
    arr[i+1].insert(0,0)
    arr[i+1].append(0)
cnt = 0
for i in range(1,T+1):
    for j in range(1,T+1):  ## 현재위치,상,하,좌,우중 현재 위치가 최대값이라면
        if arr[i][j] > max(arr[i-1][j],arr[i+1][j],arr[i][j-1],arr[i][j+1]) :
            cnt += 1
            
print(cnt)