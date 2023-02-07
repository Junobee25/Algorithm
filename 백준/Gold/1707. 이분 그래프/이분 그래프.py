from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
def bfs(V):
    Node[V] = 1
    q = deque()
    q.append(V)
    while q:
        t = q.popleft()
        for i in arr[t]:
            if Node[i]==0:
                Node[i] = -Node[t]
                q.append(i)
            else:
                if Node[i] == Node[t]:
                    return False
    return True
for i in range(k):
    n,m = map(int,input().split())
    Check = True
    arr = [[] for _ in range(n+1)]
    Node = [0 for i in range(n+1)]
    for j in range(m):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    for k in range(1,n+1):
        if Node[k] == 0:
            if not bfs(k):
                Check = False
                break
    print("YES" if Check else "NO")