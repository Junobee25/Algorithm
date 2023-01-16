import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr1 = []
arr2 = []
hash = {}
for i in range(N):
    arr1.append(input())
for j in range(M):
    arr2.append(input())

for i in arr1:
    hash[i] = 0
for j in arr2:
    if j in hash:
        hash[j] += 1
    
cnt = 0
for key,value in hash.items():
    cnt += value
print(cnt)
