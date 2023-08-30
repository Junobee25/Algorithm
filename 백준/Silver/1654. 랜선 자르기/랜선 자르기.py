import sys

input = sys.stdin.readline

K,N = map(int,input().split())


row_list = []

for i in range(K):
    t = int(input().rstrip())
    row_list.append(t)

lt = 1
rt = max(row_list)

while lt <= rt:
    mid = (lt + rt)//2
    res = 0
    for i in row_list:
        if i >= mid:
            res += (i // mid)
    if res >= N:
        lt = mid + 1
    
    else:
        rt = mid - 1

print(rt)