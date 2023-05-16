from itertools import permutations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
check = []
for i in permutations(arr,m):
    check.append(i)

check.sort()

for i in check:
    for j in i:
        print(j,end = " ")
    print()
