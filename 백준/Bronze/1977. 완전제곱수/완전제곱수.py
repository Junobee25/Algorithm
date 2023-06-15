import math

a = int(input())

b = int(input())
cnt = 0

result = []
for i in range(a,b+1):
    k = str(math.sqrt(i))
    if len(k[k.index('.'):]) == 2:
        cnt += i
        result.append(i)
if cnt == 0:
    print(-1)
else:   
    print(cnt)
    print(min(result))
