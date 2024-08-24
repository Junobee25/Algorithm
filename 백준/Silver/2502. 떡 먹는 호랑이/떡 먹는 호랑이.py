D, K = map(int, input().split())

arr = [[0, 0] for _ in range(D)]

# 피보나치 계수 초기화
arr[0] = [1, 0]
arr[1] = [0, 1]

# 피보나치 계수 계산
for i in range(2, D):
    arr[i][0] = arr[i - 1][0] + arr[i - 2][0]
    arr[i][1] = arr[i - 1][1] + arr[i - 2][1]

# 가능한 a, b 값을 탐색
for a in range(1, K // arr[D - 1][0] + 1):
    if (K - arr[D - 1][0] * a) % arr[D - 1][1] == 0:
        b = (K - arr[D - 1][0] * a) // arr[D - 1][1]
        print(a)
        print(b)
        break