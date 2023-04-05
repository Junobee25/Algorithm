import sys
input = sys.stdin.readline
n,p = map(int,input().split())
stk = [[] for _ in range(7)]
ans = 0
for _ in range(n):
    l,p = map(int,input().split())
    while stk[l] and stk[l][-1] > p:
        stk[l].pop()
        ans += 1
    if stk[l] and stk[l][-1] == p:
        continue
    stk[l].append(p)
    ans += 1
    
print(ans)