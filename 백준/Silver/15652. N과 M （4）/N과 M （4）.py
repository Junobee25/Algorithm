from itertools import combinations_with_replacement
check = set()
n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
for i in combinations_with_replacement(arr,m):
    check.add(i)
check = list(check)
check.sort()

for i in check:
    for j in i:
        print(j, end = " ")
    print()