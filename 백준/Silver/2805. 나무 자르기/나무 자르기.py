N,M = map(int,input().split())
trees = list(map(int,input().split()))

trees.sort()

lt = 1
rt = max(trees)

while lt <= rt:
    mid = (lt+rt)//2
    res = 0
    for i in trees:
        if i > mid:
            res += i - mid
            
    if res >= M:
        lt = mid + 1
    else:
        rt = mid - 1
        
print(rt)