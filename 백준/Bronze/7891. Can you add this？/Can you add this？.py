import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    print(a + b)