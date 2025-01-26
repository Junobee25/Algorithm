n = int(input())
arr = list(map(int, input().split()))

dp = [1]*len(arr)

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

result = []
t = max(dp)

for i in range(n - 1, -1, -1):
    if dp[i] == t:
        result.append(arr[i])
        t -= 1

result.reverse()
print(*result)