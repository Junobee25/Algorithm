N = int(input())
arr = list(map(int,input().split()))
arr = [0] + arr
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+arr[j])
print(dp[N])