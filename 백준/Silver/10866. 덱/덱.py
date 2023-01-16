from collections import deque
import sys

dq = deque()
n = int(input())

for i in range(n):
    arr = sys.stdin.readline().split()

    if arr[0] == "push_front":
        dq.appendleft(arr[1])
    elif arr[0] == "push_back":
        dq.append(arr[1])
    elif arr[0] == "pop_front":
        if dq:
            print(dq[0])    
            dq.popleft()
        else:
            print("-1")
    elif arr[0] == "pop_back":
        if dq:
            print(dq[len(dq) - 1])    
            dq.pop()
        else:
            print("-1")
    elif arr[0] == "size":
        print(len(dq))
    elif arr[0] == "empty":
        if dq:
            print("0")
        else:
            print("1")
    elif arr[0] == "front":
        if dq:
            print(dq[0])
        else:
            print("-1")
    elif arr[0] == "back":
        if dq:
            print(dq[len(dq) - 1])
        else:
            print("-1")