from itertools import combinations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
check = []
for i in combinations(arr,m):
    check.append(i)

for i in range(len(check)):
    check[i] = sorted(list(check[i]))
check.sort()
for i in check:
    for j in i:
        print(j,end = " ")
    print()
