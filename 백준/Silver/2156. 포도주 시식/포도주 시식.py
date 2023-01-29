import sys
input = sys.stdin.readline
N = int(input())
graph = []
for i in range(N):
    k = input().rstrip()
    graph.append(int(k))
dp = [0]*(N+1)
dp[1] = graph[0]

if N >= 2:
    dp[2] = graph[0] + graph[1]
    for i in range(3,N+1):
        dp[i] = max(dp[i-3]+sum(graph[i-2:i]), dp[i-2]+graph[i-1], dp[i-1])
print(dp[N])

