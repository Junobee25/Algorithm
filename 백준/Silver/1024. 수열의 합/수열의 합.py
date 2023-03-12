N,L = map(int,input().split())
length = 0
x = -1

for i in range(L,101):
    t = (i*i-i)//2
    if (N-t)%i == 0 and (N-t)//i>=0:
        x=(N-t)//i
        length = i
        break
if x == -1:
    print(-1)
    exit()
else:
    answer = []
    for i in range(length):
        answer.append(int(x+i))
    print(*answer)