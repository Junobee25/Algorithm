M = int(input())
N = int(input())
arr = []

for i in range(M,N+1):
    if i > 1:
        arr.append(i)
        for j in range(2,i):
            if i % j == 0 :
                arr.pop()
                break

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])