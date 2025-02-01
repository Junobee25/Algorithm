n, k = map(int, input().split())

result = [0] + [i for i in range(1, n + 1)]

# 불가능한 경우 처리
if k == n:
    print("Impossible")
    exit()
if (n - k) % 2 == 0:
    for i in range(1, n - k + 1):
        if i % 2:
            k = result[i]
            result[i] = result[i + 1]
            result[i + 1] = k
else:
    for i in range(2, n - k + 1):
        if i % 2 == 0:
            k = result[i]
            result[i] = result[i + 1]
            result[i + 1] = k
                
for i in range(1, n + 1):
    print(result[i], end = " ")
                        