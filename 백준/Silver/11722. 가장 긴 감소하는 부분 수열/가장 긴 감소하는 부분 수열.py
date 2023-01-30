# 가장 긴 증가하는 부분수열과 같은 로직
# if문만 작다고 바꿔주면됨
N = int(input())
arr = list(map(int,input().split()))
dp = [1]*N
for i in range(N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
