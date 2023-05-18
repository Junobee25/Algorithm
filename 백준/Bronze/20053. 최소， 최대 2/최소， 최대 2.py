T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    print(min(arr),max(arr))