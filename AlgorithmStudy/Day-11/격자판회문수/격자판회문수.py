arr = []
cnt = 0
for i in range(7):
    arr.append(list(map(int,input().split())))

for i in range(7):
    for j in range(3):
        if arr[i][j] == arr[i][j-3] and arr[i][j+1] == arr[i][j-4] :  # 5자리 수 => 범위 range(3) 행 대칭성 이용 
            cnt += 1
        if arr[j][i] == arr[j-3][i] and arr[j+1][i] == arr[j-4][i] :  # 5자리 수 => 범위 range(3) 열 대칭성 이용
            cnt += 1

print(cnt)

    