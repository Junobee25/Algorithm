import sys
from copy import deepcopy

input = sys.stdin.readline
row, col, test_case = map(int,input().split())
room_info = []
finedust_cnt = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]
air_cordinate = []

for _ in range(row):
    room_info.append(list(map(int,input().split())))
    
for y in range(row):
    for x in range(col):
        if room_info[y][x] == -1:
            air_cordinate.append((y,x))
        
for _ in range(test_case):

    current_room_info = deepcopy(room_info)
    movement_info = [[0] * col for _ in range(row)]
    finedust_info = [[0] * col for _ in range(row)]
    movement_info[air_cordinate[0][0]][0] = -1
    movement_info[air_cordinate[1][0]][0] = -1
    finedust_info[air_cordinate[0][0]][0] = -1
    finedust_info[air_cordinate[1][0]][0] = -1
    # 확산 조건 로직
    for i in range(row):
        for j in range(col):
            diffusion_cnt = 0
            if current_room_info[i][j] > 0:
                for k in range(4):
                    temp_y = i + dy[k]
                    temp_x = j + dx[k]
                    if 0 <= temp_y < row and 0 <= temp_x < col:
                        if (temp_y, temp_x) not in air_cordinate:
                            diffusion_cnt += 1
                            finedust_info[temp_y][temp_x] += current_room_info[i][j] // 5
                finedust_info[i][j] += current_room_info[i][j] - (current_room_info[i][j] //5 * (diffusion_cnt))

    # 공기 청정기 회전 로직 1. Head 부분
    for i in range(air_cordinate[0][0] + 1):
        for j in range(col):
            if finedust_info[i][j] != -1:
                if i == 0 and 0 < j < col:
                    movement_info[i][j + dx[3]] = finedust_info[i][j]
                if j == 0 and 0 <= i < air_cordinate[0][0] - 1:
                    # 아래쪽 향할때 공기청정기 만나면
                    if movement_info[i + dy[2]][j] == -1:
                        movement_info[i][j] = 0
                    else:
                        movement_info[i + dy[2]][j] = finedust_info[i][j]
                if i == air_cordinate[0][0] and 0 <= j < col - 1:
                    movement_info[i][j + dx[1]] = finedust_info[i][j]
                if j == col - 1 and 1 <= i <= air_cordinate[0][0]:
                    movement_info[i + dy[0]][j] = finedust_info[i][j]
                if 0 < i < air_cordinate[0][0] and 1 <= j < col - 1:
                    movement_info[i][j] = finedust_info[i][j]
    # 공기 청정기 회전 로직 2. Bottom 부분
    for i in range(air_cordinate[1][0], row):
        for j in range(col):
            if finedust_info[i][j] != -1:
                if i == air_cordinate[1][0] and 0 <= j < col - 1:
                    movement_info[i][j + dx[1]] = finedust_info[i][j]
                if air_cordinate[1][0] <= i < row - 1 and j == col - 1:
                    movement_info[i + dy[2]][j] = finedust_info[i][j]
                if i == row - 1 and 1 <= j < col:
                    movement_info[i][j + dx[3]] = finedust_info[i][j]
                if air_cordinate[1][0] < i < row and j == 0:
                    # 위쪽 향할때 공기청정기 만나면
                    if movement_info[i + dy[0]][j] == -1:
                        movement_info[i][j] = 0
                    else:
                        movement_info[i + dy[0]][j] = finedust_info[i][j]
                if air_cordinate[1][0] < i < row - 1 and 1 <= j < col - 1:
                    movement_info[i][j] = finedust_info[i][j]
    # T초마다 방의 미세먼지 정보 갱신                    
    room_info = movement_info
                    
                    
for i in range(row):
    for j in range(col):
        if room_info[i][j] > 0:
            finedust_cnt += room_info[i][j]

print(finedust_cnt)