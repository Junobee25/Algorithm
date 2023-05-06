direct = {'R' : (0,1), 'L' : (0,-1), 
          'B' : (1,0), 'T' : (-1,0),
          'RT' : (-1,1), 'LT' : (-1,-1),
          'RB' : (1,1), 'LB' : (1,-1)}
row_alpa = ['A','B','C','D','E','F','G','H']
col_num = ['1','2','3','4','5','6','7','8']
chess_board = []

# 체스판 만들기 A1 ~ H8
for i in range(8-1,-1,-1):
    location = []
    for j in range(8):
        location.append(row_alpa[j] + col_num[i])
    chess_board.append(location)

lo_king, lo_stone, n = input().split()

n = int(n)

# 초기 king위치와 stone위치 찾기
k_y, k_x = 0,0
s_y, s_x = 0,0

# 초기 king위치와 stone위치 찾기
for i in range(8):
    for j in range(8):
        if chess_board[i][j] == lo_king:
            k_y = i
            k_x = j
        if chess_board[i][j] == lo_stone:
            s_y = i
            s_x = j
            
for _ in range(n):
    let_go = input()
    if 0 <= k_y + direct[let_go][0] < 8 and 0 <= k_x + direct[let_go][1] < 8:
        if k_y + direct[let_go][0] == s_y and k_x + direct[let_go][1] == s_x:
            if 0 <= s_y + direct[let_go][0] < 8 and 0 <= s_x + direct[let_go][1] < 8:
                k_y += direct[let_go][0]
                k_x += direct[let_go][1]
                s_y += direct[let_go][0]
                s_x += direct[let_go][1]
        elif k_y + direct[let_go][0] != s_y or k_x + direct[let_go][1] != s_x:
            k_y += direct[let_go][0]
            k_x += direct[let_go][1]
print(chess_board[k_y][k_x])
print(chess_board[s_y][s_x])
