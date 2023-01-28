def DFS(L,s):
    global res
    if L == N:
        if 0<s<=k:
            res.add(s)
    else:
        DFS(L+1,s+arr[L])
        DFS(L+1,s-arr[L])
        DFS(L+1,s)

N = int(input())
arr = list(map(int,input().split()))
k = sum(arr)
res = set()
DFS(0,0)
print(k-len(res))