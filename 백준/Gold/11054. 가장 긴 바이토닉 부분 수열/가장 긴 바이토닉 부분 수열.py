N = int(input())
arr = list(map(int,input().split()))
dp_up = [1]*N
dp_down = [1]*N
dp_bi = [1]*N
# 가장 긴 증가하는 부분수열
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_up[i] = max(dp_up[i],dp_up[j]+1)

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if arr[i] > arr[j]:
            dp_down[i] = max(dp_down[i],dp_down[j]+1)

for i in range(N):
    dp_bi[i] = dp_up[i] + dp_down[i] -1

print(max(dp_bi))