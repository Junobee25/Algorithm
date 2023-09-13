N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str,arr)))
        return

    for i in range(N):
        arr.append(numbers[i])
        backtracking(depth + 1)
        arr.pop()

arr = []
backtracking(0)