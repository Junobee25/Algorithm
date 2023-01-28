import sys
input = sys.stdin.readline
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
#점화식 세운후 이차원 배열 dp로 해결
#문제 해결 아이디어 dp[a][b] a=> 자리수 b => 뒤에 오는 숫자
#뒤에오는 숫자에 따라서 경우가 나뉨 0이오는경우 2~8이오는경우 9가 나오는경우
# case 1 은 고정 case2 부터 규칙성립
for i in range(1,10):
    dp[1][i] = 1
for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%1000000000)