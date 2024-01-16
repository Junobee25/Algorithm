import sys
input = sys.stdin.readline


def check(y,x,sticker):
    r, c = len(sticker), len(sticker[0])
    if y + r > n or x + c > m:
        return False
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and board[i + y][j + x] == 1:
                return False
    return True

def stick(sticker):
    r, c = len(sticker), len(sticker[0])
    for i in range(n - r + 1):
        for j in range(m - c + 1):
            if check(i,j,sticker):
                for y in range(r):
                    for x in range(c):
                        if sticker[y][x] == 1:
                            board[i + y][j + x] = 1
                return True
    return False
                
def rotate(sticker):
    r, c = len(sticker), len(sticker[0])
    new_board = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_board[j][r - i - 1] = sticker[i][j]       
    return new_board

n, m, k = map(int,input().split())
stickers = []
for _ in range(k):
    row, col = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(row)]
    stickers.append(sticker)

board = [[0]*m for _ in range(n)]
for s in stickers:
    for _ in range(4):
        if stick(s):
            break
        s = rotate(s)
print(sum([sum(board[i]) for i in range(n)]))