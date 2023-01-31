N,M = map(int,input().split())
# dp 테이블 생성 1,2,3,4 ~ 로 놓으면 되겠지
dp = [[i for i in range(1,201)] for _ in range(200)]

# 대각선 합 점화식
for i in range(1,200):
    for j in range(1,200):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[N-1][M-1]%1000000000)
