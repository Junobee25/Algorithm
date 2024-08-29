from itertools import combinations

N = int(input())
arr = list(map(int, input().split()))

# 모든 부분 수열의 합을 집합으로 저장
res = set()
for i in range(1, N + 1):
    for c in combinations(arr, i):
        res.add(sum(c))

sorted_res = sorted(res)

i = 1
for x in sorted_res:
    if x != i:
        break
    i += 1

print(i)