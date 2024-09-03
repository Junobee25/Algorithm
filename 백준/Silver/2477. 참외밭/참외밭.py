## 동1 서2 남3 북4
## 사각형의 넓이 = 밑변 * 높이
## 북 * 서 / 북 * 동 / 남 * 서 / 남 * 동 중 최대값에서
## 남 * 동 / 남 * 서 / 북 * 동 / 북 * 서 빼면됨

n = int(input())
arr = [[0,0] for _ in range(5)] 
area = [(4,2), (4,1), (3,2), (3,1)]
i = 0

area_arr = []
for _ in range(6):
    a, b = map(int,input().split())
    area_arr.append((a,b))
    if b > arr[a][0]:
        arr[a][0] = b
        arr[a][1] = i
    i += 1

max_value = 0
width = 0
height = 0

for i in range(len(area)):
    if arr[area[i][0]][0] * arr[area[i][1]][0] > max_value:
        max_value = arr[area[i][0]][0] * arr[area[i][1]][0]
        x = arr[area[i][0]][1]
        y = arr[area[i][1]][1]
        

print((max_value - area_arr[(y + 3) % 6][1] * area_arr[(x + 3) % 6][1]) * n)