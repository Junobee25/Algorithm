N,M = map(int,input().split())
arr = [0]*N
for x in range (M) :
    i,j,k = map(int,input().split())
    for y in range (i,j+1,1) :
        arr[y-1] = k
for x in range (N) :
    print(arr[x],'',end='')