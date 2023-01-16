N = int(input())
arr = map(int,input().split())
M = int(input())
arr2 = map(int,input().split())

hash = {}
for i in arr2:
    hash[i] = 0

for i in arr:
    if i in hash:
        hash[i] = 1
for key,value in hash.items():
    print(value,end=" ")
