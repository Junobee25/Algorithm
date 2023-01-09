arr = []
max_num = 0
x = 0
y = 0
for i in range(9):
    arr.append(list(map(int,input().split())))
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            x = i
            y = j
print(max_num)
print(x+1,y+1)