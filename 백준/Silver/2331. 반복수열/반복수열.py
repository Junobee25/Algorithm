# 각자리 숫자를 P번 곱한 수들의합
A, P = map(int,input().split())
dp = [A]

point = 0 # dp 인덱스 
while True:
    K = 0 # 반복되는 순간 K값이 저장됨
    for i in str(dp[point]):
        K += int(i)**P
    point += 1
    if K in dp:
        break
    dp.append(K)
print(dp.index(K))
# 반복이 끝나는 기준은??
# 새롭게 append한 K가 dp안에 있을때 딱 그시점 인덱스
# [1,2,3,4,1,,,,,,,,,,,]



