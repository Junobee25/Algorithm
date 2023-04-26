import sys

input = sys.stdin.readline
xl = []
yl = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)
print((max(xl) - min(xl)) * (max(yl) - min(yl)))