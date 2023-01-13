import sys
input = sys.stdin.readline
T = int(input())
arr = []

for i in range(T):
    arr.append(int(input()))
arr.sort(reverse=True)
result = []

for i in range(T):
    result.append(arr[i]*(i+1))

print(max(result))