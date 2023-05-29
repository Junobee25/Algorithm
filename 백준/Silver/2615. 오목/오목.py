matrix = []

for i in range(19):
    arr = list(map(int,input().split()))
    matrix.append(arr)


dy = [-1,0,1,1]
dx = [1,1,1,0]



for i in range(19):
    for j in range(19):
        # 검은 바둑
        if matrix[i][j] == 1:
            for k in range(4):
                cnt = 1
                for t in range(1,5):
                    ny = i + dy[k]*t
                    nx = j + dx[k]*t
                    if 0 <= ny < 19 and 0 <= nx < 19:
                        if matrix[ny][nx] == 1:
                            cnt += 1
                        # 1을 발견한 인덱스에서 6개 이상이라 정답 처리 안해줬지만 정답처리 안한 오목 배열을 또 만났을 때는 우측만 비교하므로
                        # 5개라고 갯수를 카운트 할 수있기 때문에..... 이 로직은 잘못된 로직......ㅠㅠㅠㅠ
                        if matrix[ny][nx] == 0 or matrix[ny][nx] == 2:
                            break
                    if cnt == 5 and 0 <= i - dy[k] < 19 and 0 <= j - dx[k] < 19:
                        if matrix[i-dy[k]][j-dx[k]] == 1:
                            cnt = 1
                    if cnt == 5 and 0 <= i + dy[k]*5 < 19 and 0 <= j + dx[k]*5 < 19:
                        if matrix[i + dy[k]*5][j + dx[k]*5] == 1:
                            cnt = 1
                if cnt == 5:
                    print(1)
                    print(i+1,j+1)
                    exit()
        if matrix[i][j] == 2:
            for k in range(4):
                cnt = 1
                for t in range(1,7):
                    ny = i + dy[k]*t
                    nx = j + dx[k]*t
                    if 0 <= ny < 19 and 0 <= nx < 19:
                        if matrix[ny][nx] == 2:
                            cnt += 1  
                        if matrix[ny][nx] == 0 or matrix[ny][nx] == 1:
                            break     
                    if cnt == 5 and 0 <= i - dy[k] < 19 and 0 <= j - dx[k] < 19:
                        if matrix[i-dy[k]][j-dx[k]] == 2:
                            cnt = 1
                    if cnt == 5 and 0 <= i + dy[k]*5 < 19 and 0 <= j + dx[k]*5 < 19:
                        if matrix[i + dy[k]*5][j + dx[k]*5] == 2:
                            cnt = 1  
                if cnt == 5:
                    print(2)
                    print(i+1,j+1)
                    exit()

print(0)
