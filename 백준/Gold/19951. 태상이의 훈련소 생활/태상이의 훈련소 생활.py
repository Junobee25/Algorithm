n,m = map(int,input().split())

arr = list(map(int,input().split()))

temp_list = [0 for _ in range(n+1)]

for i in range(m):
    a,b,k = map(int,input().split())
    temp_list[a-1] += k
    temp_list[b] -= k

dy = 0

for i in range(n):
    dy += temp_list[i]
    print(arr[i] + dy, end = " ")