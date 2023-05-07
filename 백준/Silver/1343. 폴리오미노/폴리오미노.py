board = input().split('.')
for i in range(len(board)):
    if board[i].count("X") % 2 != 0:
        print(-1)
        exit()

for i in range(len(board)):
    if board[i].count("X") >= 4 and board[i].count("X") % 4 > 0:
        board[i] = "A" * (board[i].count("X") - board[i].count("X") % 4) + 'B' * (board[i].count("X") % 4)
    elif board[i].count("X") % 4 == 0:
        board[i] = "A"* board[i].count("X")
    else:
        board[i] = 'B'*2
result = ''
for i in board:
    result += i + '.'
print(result[:-1])
    