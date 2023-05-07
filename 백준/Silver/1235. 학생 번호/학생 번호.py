n = int(input())
id = []
for _ in range(n):
    id.append(input())
k = len(id[0])

result = 0
arr = []
for i in range(n):
    check = []
    for j in range(1,k+1):
        check.append(id[i][k-j:k])
    arr.append(check)

cnt = 0
for i in range(k):
    jungbok = []
    for j in range(n):
        jungbok.append(arr[j][i])
    
    cnt += 1
    if len(set(jungbok)) == n:
        print(cnt)
        break