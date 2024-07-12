import sys

input = sys.stdin.readline
n = int(input())

arr = []
result = 0

def search(arr, y):
    for i in reversed(range(len(arr))):
        if arr[i] == y:
            return False
        
        if arr[i] < y:
            return True
        
for i in range(n):
    x, y = map(int,input().split())
    arr.append(y)
    if len(arr) == 1:
        if arr[-1] > 0:
            result += 1
            continue
    
    else:
        k = arr.pop()
        if k == 0:
            arr = []
            continue
        if k > arr[-1]:
            result += 1
            arr.append(y)
            continue
        if k not in arr:
            result += 1
            arr.append(y)
            continue
        if k in arr:
            if search(arr, y):
                result += 1
            arr.append(y)
            continue
    
print(result)