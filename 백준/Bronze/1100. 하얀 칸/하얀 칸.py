board = []
for _ in range(8):
    board.append(list(input()))
cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0: # 홀수 칸(0부터 시작하므로)
            if board[i][j] == 'F':
                cnt += 1
        elif i % 2 != 0 and j % 2 != 0:
            if board[i][j] == 'F':
                cnt += 1
print(cnt)