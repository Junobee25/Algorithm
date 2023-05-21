n = 10

keyboard = [['q','w','e','r','t','y','u','i','o','p'],
            ['a','s','d','f','g','h','j','k','l',0],
            ['z','x','c','v','b','n','m',0,0,0]]
left_y,left_x = -1,-1
right_y,right_x = -2,-2

right_pick = ['y','u','i','o','p','h','j','k','l','b','n','m']

left,right = input().split()
result = list(input())

# 초기 위치 찾기
for i in range(3):
    for j in range(10):
        if keyboard[i][j] == left:
            left_y,left_x = i,j
        elif keyboard[i][j] == right:
            right_y,right_x = i,j


min_time = 0

for k in result:
    for i in range(3):
        for j in range(10):
            # 문자 찾고 모음이면 right움직여주기 right에서 거리재기
            if keyboard[i][j] == k:
                if k in right_pick:
                    if right_y == i and right_x == j:
                        min_time += 1
                    else:
                        min_time += (abs(i-right_y) + abs(j-right_x)) + 1
                        right_y, right_x = i,j
                else:
                    if left_y == i and left_x == j:
                        min_time += 1
                    else:
                        min_time += (abs(i-left_y) + abs(j - left_x)) + 1
                        left_y , left_x = i, j
                break
print(min_time)          