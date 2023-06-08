import sys

input = sys.stdin.readline

n,k = map(int,input().split())

coins = []

for _ in range(n):
    coins.append(int(input().rstrip()))


dp = [0 for _ in range(k+1)]

dp[0] = 1

for c in coins:
    for i in range(k+1):
        if i >= c:
            dp[i] += dp[i-c]

print(dp[k])
