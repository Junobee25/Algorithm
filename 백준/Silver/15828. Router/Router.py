import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

router = []

router = deque(router)


while True:

    info = int(input())
    if info == -1:
        break
    if len(router) == n:
        continue
    if info == 0:
        router.popleft()
    else:
        router.append(info)

if len(router) == 0:
    print("empty")
else:
    for num in router:
        print(num, end = " ")