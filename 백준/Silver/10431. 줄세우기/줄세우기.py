t = int(input())

for i in range(t):
    arr = list(map(int,input().split()))
    cnt = 0
    for a in range(2,len(arr)):
        for b in range(1,a):
            if arr[a] < arr[b]:
                k = a - b
                cnt += k
                q = arr[a]
                arr.insert(b,q)
                arr.reverse()
                arr.remove(q)
                arr.reverse()
                break
        
    print(i+1, cnt)