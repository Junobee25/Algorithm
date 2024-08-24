l = int(input())
arr = list(map(int,input().split()))
arr.sort()
n = int(input())

if n in arr:
    print(0)
else:
    s = 0
    e = 0
    
    for i in range(len(arr)):
        if arr[i] < n:
            s = arr[i]
        else:
            e = arr[i]
            break
    if n == s and n == e:
        print(0)
    else:
        s += 1
        e -= 1
        print((n - s) * (e - n + 1) + (e - n))