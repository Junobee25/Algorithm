import sys
input = sys.stdin.readline

n,m = map(int,input().split())

number_list = []

for _ in range(n):
    number_list.append(int(input()))

number_list.sort()

idx = 0
diff = number_list[n-1] - number_list[0]

for i in range(n):
    while (number_list[idx] - number_list[i] < m and idx < n - 1):
        idx += 1
    if number_list[idx] - number_list[i] >= m:
        if number_list[idx] - number_list[i] < diff:
            diff = number_list[idx] - number_list[i]

print(diff)