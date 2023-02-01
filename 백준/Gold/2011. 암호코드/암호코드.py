from collections import deque
N = list(map(int,input()))
N = deque(N)
K = len(N)
dp = [0 for _ in range(K+1)]
if N[0] == 0:
    print(0)
## bottom-up 방식으로 규칙보고
## 뒷자리부터 판단
else:
    N.appendleft(0)
    dp[0],dp[1] =1,1
    for i in range(2,K+1):
        if N[i] > 0:
            dp[i] += dp[i-1]
        tmp = N[i-1]*10 + N[i]
        if 10<=tmp<=26:
            dp[i] += dp[i-2]
    print(dp[-1]%1000000)
