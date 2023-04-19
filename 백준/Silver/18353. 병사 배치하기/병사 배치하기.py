# 문제 유형
# 가장 긴 감소하는 수열을 찾는 문제

# 접근
# 가장 긴 감소하는 수열의 길이를
# 각 원소마다 1로 두고
# 갱신된 이전의 값 중
# 자기자신 보다 크고 길이가 최대인 요소를 선택하여
# 현재 길이에 더해줌

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n

for i in range(1,n):
    max_len = -int(1e9)
    for j in range(i):
        if arr[j] > arr[i]:
            if max_len  < dp[j]:
                max_len = dp[j]
    if max_len == -int(1e9):
        pass
    else:
        dp[i] += max_len


print(n-max(dp))