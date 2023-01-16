from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
arr = []
arr = deque(arr)
for i in range(N):
    choice = input().split()
    if choice[0] == 'push':
        arr.append(int(choice[-1]))
    elif choice[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif choice[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif choice[0] == 'size':
        print(len(arr))
    elif choice[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif choice[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])