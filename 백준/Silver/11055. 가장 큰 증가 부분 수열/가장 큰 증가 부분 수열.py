N = int(input())
arr = list(map(int,input().split()))
dp = arr[:]
# dp[0] = arr[0]
# for i in range(1,N):
#     result = arr[i]
#     for k in range(i):
#         if arr[i]>arr[k]:
#             result += arr[k]
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i],result)
# print(dp)
# print(max(dp))

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+arr[i])
print(max(dp))


