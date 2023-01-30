# dp테이블엔 쌓아올린 계단의 값의 최댓값 할당
# 3번째 계단부터 로직
# 1칸 + 1칸 ,, 두칸점프
# 0,1,3,4 0,2,4
# 점화식 -> dp[i] = max(dp[i-3]+p[i-1]+p[i],dp[i-2]+p[i])
N = int(input())
M = [0]*(N+1)
for i in range(N):
    M[i] = int(input())
dp = [0]*(N+1)
# 고정값 할당
# N = 3 부터는 동적으로 테이블 생성
dp[0] = M[0]
dp[1] = M[0]+M[1]
if N>=2:
    dp[2] = max(M[0]+M[2],M[1]+M[2])
for i in range(3,N):
    dp[i] = max(dp[i-3]+M[i-1]+M[i],dp[i-2]+M[i])
print(dp[N-1])