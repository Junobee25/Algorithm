from collections import deque
N = int(input())
arr = [i for i in range(1,N+1)]
arr = deque(arr)


while True:
    if N == 1:
        print(arr.popleft())
        break
    arr.popleft()
    if len(arr) == 1:
        print(arr[0])
        break
    arr.append(arr.popleft())