N = int(input())
my = []
for i in range(N):
    arr = list(map(str,input().split()))
    arr[1] = int(arr[1])
    arr[2] = int(arr[2])
    arr[3] = int(arr[3])
    my.append(arr)

my.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))
for i in range(N):
    print(my[i][0])