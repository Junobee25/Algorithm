n = int(input())

deci = [False, False] + [True] * (n - 1)

deci_num = []

for i in range(2, n + 1):
    if deci[i]:
        for j in range(2*i, n + 1, i):
            deci[j] = False

for i in range(2, len(deci)):
    if deci[i]:
        deci_num.append(i)

cnt = 0
interval_sum = 0
end = 0

for start in range(len(deci_num)):
    while interval_sum < n and end < len(deci_num):
        interval_sum += deci_num[end]
        end += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= deci_num[start]

print(cnt)