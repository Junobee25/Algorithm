import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

heapq.heapify(arr)

for i in range(n):
    k = int(input().rstrip())
    if k == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))

    elif k > 0:
        heapq.heappush(arr, k)