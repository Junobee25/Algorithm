T = int(input())
arr = []
for i in range(T):
    a = list(map(int,input().split()))
    arr.append(a)

for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] <j[1]:
            cnt +=1
    print(cnt, end = " ")