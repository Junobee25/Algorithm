import sys

input = sys.stdin.readline

n,m = map(int,input().split())



check = {}
result_cnt = 0

result = []
for _ in range(n):
    check[input().rstrip()] = 1

for _ in range(m):
    k = input().rstrip()
    if k in check:
        result_cnt += 1
        result.append(k)
result.sort()
print(result_cnt)
for i in range(len(result)):
    print(result[i])

    