T = int(input())
for i in range(T):
    N = int(input())
    arr = [1,1,1]

    for i in range(N):
        arr.append(arr[i]+arr[i+1])
    print(arr[N-1])