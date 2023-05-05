n = int(input())
arr = list(map(int,input().split()))
arr = set(arr)
arr = list(arr)
arr.sort()
for i in arr:
    print(i, end = " ")