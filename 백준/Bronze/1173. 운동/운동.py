# N은 해야되는 운동 시간
# m은 최소 맥박 적어지면 m으로 고정
# M은 최대 맥박 넘어가면 안됨
# T는 운동했을 때 더해지는 맥박
# R은 휴식했을 때 줄어드는 맥박
from copy import deepcopy
N,m,M,T,R = map(int,input().split())
if M - m < T:
    print(-1)
    exit()
# 맥박수를 계산하기 위해 deepcopy m은 비교해야되므로 그대로 둬야함
check_min_m = deepcopy(m)

# 운동카운트 변수인 doing이 N이되면 break
doing = 0 
# 운동과 휴식할 때 카운트를 해줄 결과 변수
result = 0
while True:
    # 운동
    if check_min_m + T <= M:
        doing += 1
        result += 1
        check_min_m += T
    # 휴식
    else:
        if check_min_m + T >= M:
            if check_min_m - R <= m:
                check_min_m = m
                result += 1
            else:
                check_min_m -= R
                result += 1

    if doing == N:
        break
print(result)