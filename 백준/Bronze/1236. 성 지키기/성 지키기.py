n,m = map(int,input().split())

arr1 = []
for _ in range(n):
    k = list(input())
    arr1.append(k)
row = 0
for i in range(n):
    if all(k == '.' for k in arr1[i]):
        row += 1

col = 0
for i in range(m):
    cnt = 0
    for j in range(n):
        if arr1[j][i] == '.':
            cnt += 1

    if cnt == n:
        col += 1

print(max(row,col))
