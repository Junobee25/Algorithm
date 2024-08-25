t = int(input())

for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    temp_dict = {}
    result = 0
    for _ in range(n):
        x, y, r = map(int,input().split())
        if (x - x1)**2 + (y - y1)**2 < r**2:
            if (x, y, r) in temp_dict:
                temp_dict[(x,y,r)] = 0
            else:
                temp_dict[(x,y,r)] = 1
                
        if (x - x2)**2 + (y - y2)**2 < r**2:
            if (x, y, r) in temp_dict:
                temp_dict[(x,y,r)] = 0
            else:
                temp_dict[(x,y,r)] = 1
    for v in temp_dict.values():
        result += v
    print(result)
    