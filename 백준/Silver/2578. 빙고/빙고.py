board = [[0] * 5 for _ in range(5)]

for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        board[i][j] = arr[j]

bingo_cnt = 0
cnt = 0
pick_list = []

# 방문처리
check_row = [True] * 5
check_col = [True] * 5
check_dae = True
check_dae2 = True


def check_bingo(board):
    global bingo_cnt
    global check_row
    global check_col
    global check_dae
    global check_dae2
    # 가로 체크
    for i in range(5):
        if check_row[i]:
            if all(board[i][k] == 1 for k in range(5)):
                check_row[i] = False
                bingo_cnt += 1
    # 세로체크
    for i in range(5):
        if check_col[i]:
            if all(board[k][i] == 1 for k in range(5)):
                check_col[i] = False
                bingo_cnt += 1
    # 대각선체크
    if check_dae:
        if all(board[k][k] == 1 for k in range(5)):
            check_dae = False
            bingo_cnt += 1
    if check_dae2:
        if all(board[k][4 - k] == 1 for k in range(5)):
            check_dae2 = False
            bingo_cnt += 1
    return bingo_cnt


for i in range(5):
    pick_list.append(list(map(int, input().split())))

for i in range(5):
    for a in range(5):
        cnt += 1
        for y in range(5):
            for x in range(5):
                if board[y][x] == pick_list[i][a]:
                    board[y][x] = 1
                if check_bingo(board) >= 3:
                    print(cnt)
                    exit()