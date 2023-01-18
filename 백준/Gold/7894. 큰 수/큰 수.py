import math
T = int(input())
for i in range(T):
    K = int(input())
    result = 0
    for j in range(1,K+1):
        result+=math.log10(j)
    print(int(result+1))


# 팩토리얼 직접 구현 후 시간초과 나서 상용로그로 풀이