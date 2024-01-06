import sys
import heapq
input = sys.stdin.readline

N = int(input())
max_heap = []

for _ in range(N):
    info = int(input())

    if not info:
        if len(max_heap) == 0:
            print(0)

        else:
            print(-heapq.heappop(max_heap))

    else:
        heapq.heappush(max_heap, -info)