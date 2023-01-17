A,B = map(int,input().split())
arr = []
cnt = 1
for i in range(1,1001):
    for j in range(i):
        arr.append(cnt)
    cnt +=1
print(sum(arr[A-1:B]))