n = int(input())
import sys
input = sys.stdin.readline
arr = []
for i in range(n):
    a = int(input().rstrip())
    arr.append(a)

arr.sort(reverse=True)
for i in arr:
    print(i)