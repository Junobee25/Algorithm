N,M = map(int,input().split())
tree = list(map(int,input().split()))

lt = 1
rt = max(tree)
while lt<=rt:
    mid = (lt+rt)//2 
    res = 0
    for i in tree:
        if i > mid:
            res += i - mid
    if res>=M:
        
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)