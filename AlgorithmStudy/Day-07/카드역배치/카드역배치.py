import sys
input = sys.stdin.readline
a = list(range(21))

for _ in range(10):
    s, e = map(int,input().split())
    # 요소를 뒤집을 때 반복이 되는 횟수를 계산하는 법이 중요함
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)

for x in a:
    print(x, end=" ")