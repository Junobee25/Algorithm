def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2,end="")


n = int(input(),2)
n = n*17
DFS(n)