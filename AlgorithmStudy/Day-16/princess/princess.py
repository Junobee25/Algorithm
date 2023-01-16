from collections import deque
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
arr = deque(arr)
queue = []

cnt = 1
counting = 0
while counting <= N-1:
    a = arr.popleft()
    arr.append(a)
    cnt += 1
    if cnt == M:
        queue.append(arr.popleft())
        cnt = 1
        counting += 1
print(queue[-1])

    


