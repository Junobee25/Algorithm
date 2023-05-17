dy = [-2,-1,1,2,2,1,-1,-2]
dx = [1,2,2,1,-1,-2,-2,-1]

x = ['A','B','C','D','E','F']
y = ['1','2','3','4','5','6']
dy_dx_idx = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
board = [[0]*6 for _ in range(6)]
idx = {}

for i in range(6):
    for j in range(6):
        board[i][j] = x[j] + y[i]
        idx[board[i][j]] = (i,j)

visited = [[0]*6 for _ in range(6)]

first_idx = 0
last_idx = 0

cnt = 0

check_fail = 0
flag2 = True
for _ in range(36):
    cnt += 1
    check = input()
    visited[idx[check][0]][idx[check][1]] += 1
    if cnt == 1:
        first_idx = idx[check]
    if cnt > 1:
        if (idx[check][0]-check_fail[0],idx[check][1]-check_fail[1]) not in dy_dx_idx:
            flag2 = False
    if cnt == 36:
        last_idx = idx[check]
    check_fail = idx[check]



for i in range(6):
    for j in range(6):
        if visited[i][j] != 1:
            print("Invalid")
            exit()
        

flag = False
for i in range(8):
    ny = last_idx[0] + dy[i]
    nx = last_idx[1] + dx[i]
    if 0 <= ny < 6 and 0 <= nx < 6:
        if ny == first_idx[0] and nx == first_idx[1]:
            flag = True

if flag == False or flag2 == False:
    print("Invalid")
else:
    print("Valid")