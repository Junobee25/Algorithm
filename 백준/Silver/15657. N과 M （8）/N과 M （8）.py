N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()

def backtracking(depth):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return

    for i in range(depth,N):
        arr.append(numbers[i])
        backtracking(i)
        arr.pop()

arr = []
backtracking(0)