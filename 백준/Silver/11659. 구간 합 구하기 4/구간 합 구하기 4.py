import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0]
temp = 0
for i in arr:
    temp+=i
    prefix.append(temp)
for i in range(M):
    a,b = map(int,input().split())
    print(prefix[b]-prefix[a-1])