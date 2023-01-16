def DFS(x,y):
    if y == 1:
        return x%C
    else:
        res = DFS(x,y//2)
        if y%2 ==0:
            return res*res%C
        else:
            return res*res*x%C

A,B,C = map(int,input().split())
print(DFS(A,B))
