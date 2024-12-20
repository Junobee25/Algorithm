T = int(input())


for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    a = (x1 - x2)**2
    b = (y1 - y2)**2
    r = (a + b)**(1/2)
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 + r2 > r and abs(r2 - r1) < r:
            print(2)
        elif r1 + r2 == r or abs(r2 - r1) == r:
            print(1)
        else:
            print(0)