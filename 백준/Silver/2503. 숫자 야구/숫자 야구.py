# 3자리 순열로 만들 수 있는 모든 숫자를 구한다
# 입력으로 주어진 s과 b의 값과 일치하면 계속 진행 += 1
# 다르면 다른 숫자로 넘어감
# 사람의 직관으로 맞추는 것이 아니라
# 모든 경우의 수에서 입력으로 주어진 s,b조합과 비교하여 일치하는 숫자를 찾는다
# 컴퓨팅적 사고
from itertools import permutations
n = int(input())

strike_ball = []
for _ in range(n):
    num,s,b = input().split()
    s = int(s)
    b = int(b)
    strike_ball.append((num,s,b))


num_list = [1,2,3,4,5,6,7,8,9]
condition = 0
for p in permutations(num_list,3):
    check = 0
    for info in strike_ball: # info 에는 이 숫자는 몇 s 몇 b이다 라는 정보가 들어있음
        is_st,is_ba = 0,0
        number,st,ba = info[0],info[1],info[2]

        for i in range(len(number)): # number는 입력으로 주어진 숫자들
            if p[i] == int(number[i]):
                is_st += 1
            elif (int(number[i]) in p) and (p[i] != int(number[i])):
                is_ba += 1
        if is_st == st and is_ba == ba:
            check += 1

    if check == n:
        condition += 1
print(condition)
