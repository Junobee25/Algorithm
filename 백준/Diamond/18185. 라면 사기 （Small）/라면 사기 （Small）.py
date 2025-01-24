n = int(input())
arr = list(map(int, input().split())) + [0,0]
result = 0
for i in range(n):
    if arr[i+1] > arr[i+2]:
        k = min(arr[i], arr[i+1] - arr[i+2])
        arr[i]-=k
        arr[i+1]-=k
        result += 5*k

        k2 = min(arr[i], arr[i+1], arr[i+2])
        arr[i] -= k2
        arr[i+1] -= k2
        arr[i+2] -= k2
        result += 7*k2
    else:
        k3 = min(arr[i], arr[i+1], arr[i+2])
        arr[i] -= k3
        arr[i+1] -= k3
        arr[i+2] -= k3
        result += 7*k3

        k4 = min(arr[i], arr[i+1])
        arr[i] -= k4
        arr[i+1] -= k4
        result += 5*k4
        
    result += 3*arr[i]

print(result)