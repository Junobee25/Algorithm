n,m = map(int,input().split())
board = []

for _ in range(n):
    k = list(input())
    board.append(k)

board_B = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]

board_W = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]




result = 9999999
cnt = 0
for i in range(n-7):
    for j in range(m-7):
        check = []
        for y in range(i,i+8):
            k = []
            for x in range(j,j+8):
                k.append(board[y][x])
            check.append(k)

        cnt_b = 0
        cnt_w = 0
        for a in range(8):
            for b in range(8):
                if board_B[a][b] != check[a][b]:
                    cnt_b += 1



        for a in range(8):
            for b in range(8):
                if board_W[a][b] != check[a][b]:
                    cnt_w += 1


        choice = min(cnt_b,cnt_w)
        if result > choice:
            result = choice
print(result)