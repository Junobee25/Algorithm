# dp[6] = dp[4]*3 + dp[2]*2 + dp[0]*2 로 점화식 유추

N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1
for i in range(2,N+1,2):
    dp[i] = dp[i-2]*3
    for j in range(0,i-2,2):
        dp[i] += dp[j]*2
print(dp[N])