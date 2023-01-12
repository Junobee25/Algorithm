T = int(input())
body = []
for i in range(T):
    a,b = map(int,input().split())
    body.append((a,b))
body.sort(reverse=True)

largest = 0
cnt = 0
for x,y in body:
    if y>largest:
        largest = y
        cnt += 1