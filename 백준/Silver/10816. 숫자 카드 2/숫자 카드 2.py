N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))

hash = {}
for i in arr1:
    if i in hash:
        hash[i] += 1
    else:
         hash[i] = 1

for i in arr2:
    if i in hash:
        print(hash[i],end=' ')
    else:
        print(0,end=' ')