import sys

input = sys.stdin.readline

# 물품의 수 N, 버틸수 있는 무게 K
n, k = map(int, input().rstrip().split())

# 각 물품의 무게와 가치를 저장하는 리스트
items = []

for _ in range(n):
    w, v = map(int, input().rstrip().split())
    items.append((w, v))

# dp 배열 초기화
dp = [0] * (k + 1)

# 물품을 하나씩 고려하면서 dp 배열 업데이트
for i in range(n):
    w, v = items[i]
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

# 최대 가치 출력
print(dp[k])