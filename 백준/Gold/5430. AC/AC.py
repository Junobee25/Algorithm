from collections import deque

T = int(input())

for _ in range(T):
    cmd = input().rstrip()
    n = int(input())
    str_arr = input().rstrip()[1:-1].split(',')

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, str_arr))

    direction = 'left'
    error = False

    for run in cmd:
        if run == 'R':
            if direction == 'left':
                direction = 'right'
            else:
                direction = 'left'
        elif run == 'D':
            if len(arr) == 0:
                error = True
                break
            if direction == 'left':
                arr.popleft()
            else:
                arr.pop()

    if error:
        print("error")
    else:
        if direction == 'right':
            arr.reverse()
        print('[', end='')
        print(','.join(map(str, arr)), end='')
        print(']')