from collections import deque
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
arr = deque(arr)
queue = []

cnt = 1
counting = 0
while counting <= N-1:
    if N == 1 and M == 1:
        queue.append(arr.popleft())
        print(str(queue).replace('[', '<').replace(']', '>'))
        break
    elif M == 1:
        print("<", end="")
        for i in range(len(arr)-1):
            print(arr[i],end =", ")
        print(str(arr[-1])+">")
        break
    a = arr.popleft()
    arr.append(a)
    cnt += 1
    if cnt == M:
        queue.append(arr.popleft())
        cnt = 1
        counting += 1
if M!=1:
    print(str(queue).replace('[', '<').replace(']', '>'))
