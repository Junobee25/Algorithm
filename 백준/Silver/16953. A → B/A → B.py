n, m = map(int,input().split())

cnt = 0
flag = False
while m >= n:
    if m % 10 == 1:
        m //= 10
        cnt += 1
        
    elif m % 2 == 0:
        m //= 2
        cnt += 1
        
    if n == m:
        cnt += 1
        flag = True
        break
        
    if m % 10 != 1 and m % 2 != 0:
        break
    
if flag:
    print(cnt)
else:
    print(-1)